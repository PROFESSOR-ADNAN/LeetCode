class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # def isValid(val):
        #     condition = [True] * len(houses)
        #     for heater in heaters:
        #         for house in houses:
        #             if abs(val - house) > heater:
                        


        # low, high = len(houses)//2, len(houses)-1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return low
        
        # house_left = min(houses)
        # house_right = max(houses)

        # def isValid(val):
        #     mn_left = float("inf")
        #     mx_right = float("-inf")

        #     left = float("-inf")
        #     right = float("inf")

        #     for heater in heaters:
        #         left = max(left, heater - val)
        #         mn_left = min(mn_left, heater-val)
        #         right = min(left, heater + val)
        #         mx_right = max(mx_right, heater+val)

        #     return left <= right and mn_left <= house_left and mx_right >= house_right

        # low, high = 0, max(max(houses), max(heaters))
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return low

        # def isValid(val):
        #     ranges = []
        #     for heater in heaters:
        #         ranges.append([heater-val, heater+val])

        #     covered = set()
        #     for house in houses:
        #         for interval in ranges:
        #             if interval[0] <= house <= interval[1]:
        #                 covered.add(house)
        #                 break
            
        #     return len(covered) == len(houses)

        # low, high = 0, max(max(houses), max(heaters))
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return low


        # mx = float("-inf")
        # for house in houses:
        #     mn = float("inf")
        #     for heater in heaters:
        #         mn = min(mn, abs(house - heater))

        #     mx = max(mx, mn)

        # return mx

        # heaters.sort()
        # mx = float("-inf")

        # for house in houses:
        #     left, right = 1, max(heaters)
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if house 
        #         elif house < heaters[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #     print(house, heaters[mid])
        #     mx = max(mx, abs(house - left))

        # return mx

        def mn_distance_between_house_nearest_heater(heaters, house):
            left, right = 0, len(heaters)-1
            mn_dist = float("inf")
            while left <= right:
                mid = left + (right - left) // 2
                mn_dist = min(mn_dist, abs(house - heaters[mid]))
                if house < heaters[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return mn_dist

        heaters.sort()
        radius = float("-inf")
        for house in houses:
            radius = max(radius, mn_distance_between_house_nearest_heater(heaters, house))

        return radius
