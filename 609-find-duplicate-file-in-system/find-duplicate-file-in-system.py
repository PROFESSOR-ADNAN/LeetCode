class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        textToPath = defaultdict(list)
        for path in paths:
            files = list(path.split())
            root_path = files[0]
            files = files[1:]

            for file_ in files:
                start_ind = file_.index("(")
                end_ind = file_.index(")")
                text = file_[start_ind+1:end_ind]
                file_name = file_[:start_ind]
                file_path = root_path + "/" + file_name

                textToPath[text].append(file_path)

        ans = []
        for path in textToPath.values():
            if len(path) > 1:
                ans.append(path)

        return ans

