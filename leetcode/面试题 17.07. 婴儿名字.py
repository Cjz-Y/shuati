from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:

        name_value = {}
        father = {}

        for name in names:
            first = name.index('(')
            second = name.index(')')
            key = name[:first]
            value = name[first + 1:second]
            name_value[key] = int(value)
            father[key] = key


        ans = set()
        for synonym in synonyms:
            l = synonym.split(',')
            one = l[0].replace('(', '')
            two = l[1].replace(')', '')

            if one not in father.keys():
                father[one] = one
                name_value[one] = 0
            if two not in father.keys():
                father[two] = two
                name_value[two] = 0


            father_one = one
            while father[father_one] != father_one:
                father[father_one] = father[father[father_one]]
                father_one = father[father[father_one]]

            father_two = two
            while father[father_two] != father_two:
                father[father_two] = father[father[father_two]]
                father_two = father[father[father_two]]

            if father_one > father_two:
                father_one, father_two = father_two, father_one

            ans.add(father_one)
            if father_two in ans:
                ans.remove(father_two)
            name_value[father_one] += name_value[father_two]
            father[father_two] = father_one

        for name in names:
            first = name.index('(')
            key = name[:first]
            if father[key] == key:
                ans.add(key)

        result = [key + "(" + str(name_value[key]) + ")" for key in ans]


        return result











