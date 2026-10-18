class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = []
        self.t_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t_map or not len(self.t_map[key]):
            return ""
        val_list = self.t_map[key]
        l, r = 0, len(val_list) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if val_list[m][0] <= timestamp:
                res = val_list[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

