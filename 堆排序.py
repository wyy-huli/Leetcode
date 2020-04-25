# Leetcode
Leetcode-Python-Soultion
from collections import deque #双端队列，可以在列表两端操作，进行添加和删除操作
def swap_param(L, i, j): #i，j位置上的元素交换
    L[i], L[j] = L[j], L[i]
    return L
def heap_adjust(L, start, end):
    temp = L[start]
    i = start #父节点
    j = 2 * i #左孩子结点
    while j <= end: #查看孩子结点所在位置是否越界
        if (j < end) and (L[j] < L[j + 1]): #左孩子小于右孩子
            j += 1
        if temp < L[j]: #父节点小于左孩子
            L[i] = L[j]#父节点位置的元素换成左孩子
            i = j # 父节点与左孩子的位置索引互换，j还是左孩子的索引
            j = 2 * j #看是否还有左孩子
        else:
            break
    L[i] = temp #保证没有结点丢失（与while语句里面的第二if结合）
def heap_sort(L):
    L_length = len(L) - 1
    first_sort_count = L_length // 2
    for i in range(first_sort_count):#将序列元素调整为大根堆
        heap_adjust(L, first_sort_count - i, L_length)
    for i in range(L_length - 1):#把堆顶元素和堆末尾的元素交换，把剩余的元素调整为大根堆·
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)
    return [L[i] for i in range(1, len(L))]

def main():
    L = deque([3,5,7,2,33,4,2,4,9,94,4])
    L.appendleft(0)
    print (heap_sort(L))
if __name__ == '__main__':
    main()
