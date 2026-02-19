class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainToCount = defaultdict(int)
        for cpdomain in cpdomains:
            domains = cpdomain.split()
            count = int(domains[0])

            domains = domains[1].split(".")

            for i in range(len(domains)-1, -1, -1):
                subDomain = ".".join(domains[i:])
                domainToCount[subDomain] += count

        ans = []
        for sub_domain, count in domainToCount.items():
            cp_domain = str(count) + " " + sub_domain
            ans.append(cp_domain)

        return ans
