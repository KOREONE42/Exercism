import json

class RestAPI:
    def __init__(self, database=None):
        if database is None:
            database = {"users": []}
        self.database = database

    def find_user(self, name):
        for user in self.database["users"]:
            if user["name"] == name:
                return user
        return None

    def update_balance(self, user):
        # calculate balance as (total owed_by) - (total owes)
        user["balance"] = round(sum(user["owed_by"].values()) - sum(user["owes"].values()), 2)

    def get(self, url, payload=None):
        if url == "/users":
            # If payload is given, filter the users that are requested.
            if payload:
                data = json.loads(payload)
                # Filter users by the given names and sort by name.
                filtered_users = [
                    user for user in self.database["users"] if user["name"] in data["users"]
                ]
                sorted_users = sorted(filtered_users, key=lambda u: u["name"])
            else:
                # Otherwise, return all users sorted by name.
                sorted_users = sorted(self.database["users"], key=lambda u: u["name"])
            return json.dumps({"users": sorted_users})
        else:
            return None

    def post(self, url, payload=None):
        if url == "/add":
            data = json.loads(payload)
            new_user_name = data["user"]
            # Create a new user object.
            new_user = {
                "name": new_user_name,
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        
        elif url == "/iou":
            data = json.loads(payload)
            lender_name = data["lender"]
            borrower_name = data["borrower"]
            amount = data["amount"]

            # Retrieve the user objects.
            lender = self.find_user(lender_name)
            borrower = self.find_user(borrower_name)

            # If there is a reverse IOU (i.e. lender owes borrower), cancel it out.
            if borrower_name in lender["owes"]:
                existing = lender["owes"][borrower_name]
                if amount < existing:
                    # Subtract the new amount from the existing reverse debt.
                    new_debt = round(existing - amount, 2)
                    lender["owes"][borrower_name] = new_debt
                    borrower["owed_by"][lender_name] = new_debt
                elif amount == existing:
                    # Cancel out completely.
                    del lender["owes"][borrower_name]
                    del borrower["owed_by"][lender_name]
                else:
                    # New IOU exceeds the old reverse debt.
                    remaining = round(amount - existing, 2)
                    del lender["owes"][borrower_name]
                    del borrower["owed_by"][lender_name]
                    # Now add the remaining amount to the normal direction.
                    if borrower_name in lender["owed_by"]:
                        lender["owed_by"][borrower_name] += remaining
                        borrower["owes"][lender_name] += remaining
                    else:
                        lender["owed_by"][borrower_name] = remaining
                        borrower["owes"][lender_name] = remaining
            else:
                # No reverse IOU exists.
                if borrower_name in lender["owed_by"]:
                    # Already exists, so just add the new amount.
                    lender["owed_by"][borrower_name] += amount
                    borrower["owes"][lender_name] += amount
                else:
                    # Create new record.
                    lender["owed_by"][borrower_name] = amount
                    borrower["owes"][lender_name] = amount

            # Update the balances.
            self.update_balance(lender)
            self.update_balance(borrower)

            # Prepare response: include only the affected users, sorted by name.
            response_users = sorted([lender, borrower], key=lambda u: u["name"])
            return json.dumps({"users": response_users})
        else:
            return None
