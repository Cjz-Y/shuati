from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        father = {}
        childs = {}

        for i in range(len(accounts)):

            childs[i] = []
            account = accounts[i]

            print('index = %d,  name = %s' % (i, account[0]))

            child_father = []
            child_father_use = set()

            account = set(account[1:])

            # 遍历所有的儿子，找找他们的其他父亲，可能有多个父亲，将所有父亲合并到第一个父亲上
            for item_account in account:

                temp_father = father.get(item_account, None)
                # print('account = %s, father = %s' % (item_account, str(temp_father)))
                # item_account 是有父亲的
                if temp_father is not None:
                    if temp_father not in child_father_use:
                        child_father.append(temp_father)
                        child_father_use.add(temp_father)
                # 是没父亲的，所以指向当前的父亲
                else:
                    father[item_account] = i
                    childs[i].append(item_account)

            print('child_father length is %s' % child_father)

            # 判断儿子中是否已经有了其他父亲，如果有了，就把所有的都指向第一个父亲
            if child_father:
                child_father.append(i)
                root = child_father[0]
                print('root : %d' % root)
                for j in range(1, len(child_father)):
                    other_father = child_father[j]
                    print('other_father = %d' % other_father)

                    # 父亲重定向
                    for child in childs[other_father]:
                        father[child] = root

                    # 把所有的节点都放在root下
                    childs[root].extend(childs[other_father])
                    childs.pop(other_father)

        ans = []
        for key, value in childs.items():
            temp_ans = []
            temp_ans.append(accounts[key][0])
            value.sort()
            temp_ans.extend(value)
            ans.append(temp_ans)

        return ans