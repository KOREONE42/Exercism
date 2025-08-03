type EqualFn<T> = (a: T, b: T) => boolean;
type GetterFn<T> = () => T;
type SetterFn<T> = (val: T) => T;
type UpdateFn<T> = (prevValue?: any) => any;
type UnsubscribeFn = () => void;

interface Node<T> {
  name?: string;
  value: T;
  equalFn: EqualFn<T>;
  subscribers: Set<Observer<any>>;
}

interface ComputedCell<T> extends Node<T> {
  computeFn: (prev?: T) => T;
  deps: Set<Node<any>>;
}

interface CallbackNode<T> {
  updateFn: (prev?: T) => T;
  lastValue?: T;
  deps: Set<Node<any>>;
}

type Observer<T> = ComputedCell<T> | CallbackNode<T>;

let activeObserver: Observer<any> | null = null;

function isComputed<T>(obs: Observer<T>): obs is ComputedCell<T> {
  return (obs as ComputedCell<T>).computeFn !== undefined;
}

function trackDependency<T>(node: Node<T>) {
  if (activeObserver) {
    node.subscribers.add(activeObserver);
    activeObserver.deps.add(node);
  }
}

function propagate(changed: Node<any>[]) {
  const computedQueue: ComputedCell<any>[] = [];
  const callbackQueue: CallbackNode<any>[] = [];
  const enqueuedComp = new Set<ComputedCell<any>>();
  const enqueuedCb = new Set<CallbackNode<any>>();

  // seed queues
  for (const node of changed) {
    for (const obs of node.subscribers) {
      if (isComputed(obs)) {
        if (!enqueuedComp.has(obs)) {
          enqueuedComp.add(obs);
          computedQueue.push(obs);
        }
      } else {
        if (!enqueuedCb.has(obs)) {
          enqueuedCb.add(obs);
          callbackQueue.push(obs);
        }
      }
    }
  }

  // process computed cells
  while (computedQueue.length) {
    const cell = computedQueue.shift()!;
    enqueuedComp.delete(cell);
    // unsubscribe old deps
    for (const dep of cell.deps) {
      dep.subscribers.delete(cell);
    }
    cell.deps.clear();
    // recompute value
    const prevObs = activeObserver;
    activeObserver = cell;
    const oldVal = cell.value;
    const newVal = cell.computeFn(oldVal);
    activeObserver = prevObs;
    if (!cell.equalFn(oldVal, newVal)) {
      cell.value = newVal;
      // enqueue downstream observers
      for (const obs of cell.subscribers) {
        if (isComputed(obs)) {
          if (!enqueuedComp.has(obs)) {
            enqueuedComp.add(obs);
            computedQueue.push(obs);
          }
        } else {
          if (!enqueuedCb.has(obs)) {
            enqueuedCb.add(obs);
            callbackQueue.push(obs);
          }
        }
      }
    }
  }

  // process callbacks once
  for (const cb of callbackQueue) {
    // unsubscribe old deps
    for (const dep of cb.deps) {
      dep.subscribers.delete(cb);
    }
    cb.deps.clear();
    // run callback
    const prevObs = activeObserver;
    activeObserver = cb;
    cb.lastValue = cb.updateFn(cb.lastValue);
    activeObserver = prevObs;
  }
}

function createInput<T>(
  initial: T,
  equal?: boolean | EqualFn<T>,
  options?: { name?: string }
): [GetterFn<T>, SetterFn<T>] {
  let equalFn: EqualFn<T>;
  if (typeof equal === 'function') equalFn = equal as EqualFn<T>;
  else if (equal === true) equalFn = (a, b) => a === b;
  else equalFn = () => false;

  const subject: Node<T> = {
    name: options?.name,
    value: initial,
    equalFn,
    subscribers: new Set(),
  };

  const getter: GetterFn<T> = () => {
    trackDependency(subject);
    return subject.value;
  };

  const setter: SetterFn<T> = (newVal: T) => {
    const oldVal = subject.value;
    if (!subject.equalFn(oldVal, newVal)) {
      subject.value = newVal;
      propagate([subject]);
    }
    return subject.value;
  };

  return [getter, setter];
}

function createComputed<T>(
  updateFn: (prev?: T) => T,
  initial?: T,
  equal?: boolean | EqualFn<T>,
  options?: { name?: string }
): GetterFn<T> {
  let equalFn: EqualFn<T>;
  if (typeof equal === 'function') equalFn = equal as EqualFn<T>;
  else if (equal === true) equalFn = (a, b) => a === b;
  else equalFn = () => false;

  const cell: ComputedCell<T> = {
    name: options?.name,
    value: initial as T,
    equalFn,
    subscribers: new Set(),
    computeFn: updateFn,
    deps: new Set(),
  };

  // initial compute (subscribe to dependencies)
  const prevObs = activeObserver;
  activeObserver = cell;
  cell.value = updateFn(cell.value);
  activeObserver = prevObs;

  const getter: GetterFn<T> = () => {
    trackDependency(cell);
    return cell.value;
  };

  return getter;
}

function createCallback<T>(
  updateFn: (prev?: T) => T,
  initial?: T
): UnsubscribeFn {
  const cb: CallbackNode<T> = {
    updateFn,
    lastValue: initial,
    deps: new Set(),
  };
  // initial run (subscribe)
  const prevObs = activeObserver;
  activeObserver = cb;
  cb.lastValue = updateFn(cb.lastValue);
  activeObserver = prevObs;

  return () => {
    for (const dep of cb.deps) {
      dep.subscribers.delete(cb);
    }
    cb.deps.clear();
  };
}

export { createInput, createComputed, createCallback };