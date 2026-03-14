class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.homePage = Node(homepage)
        self.currPage = self.homePage

    def visit(self, url: str) -> None:
        newPage = Node(url, None, self.currPage)

        self.currPage.next = newPage
        self.currPage = newPage

    def back(self, steps: int) -> str:
        curr = self.currPage
        while curr.prev and steps > 0:
            curr = curr.prev
            steps -= 1

        self.currPage = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.currPage
        while curr.next and steps > 0:
            curr = curr.next
            steps -= 1
        
        self.currPage = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)