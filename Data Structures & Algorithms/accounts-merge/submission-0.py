class EmailUnion:
    def __init__(self, accounts):


        # Variable initialization
        self.parent = {}
        self.accountName = {}
        self.rank = {}

        # Assign appropriate values for variable
        for account in accounts:
            # Data pre-processing
            accountName = account[0]
            emailsList = account[1:]
            for email in emailsList:
                self.parent[email] = email
                self.accountName[email] = accountName
                self.rank[email] = 0

    def find(self, email):
        if email != self.parent[email]:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, email1, email2):
        p1, p2 = self.find(email1), self.find(email2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        emailUnion = EmailUnion(accounts)
        for account in accounts:
            firstEmail = account[1]
            for email in account[2:]:
                emailUnion.union(firstEmail, email)

        emailGroups = defaultdict(list)
        for email in emailUnion.parent:
            root = emailUnion.find(email)
            emailGroups[root].append(email)

        for root, emails in emailGroups.items():
            name = emailUnion.accountName[root]
            res.append([name] + sorted(emails))

        return res
