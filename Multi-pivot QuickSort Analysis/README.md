# Multi-pivot QuickSort Analysis

QuickSort [1] has been implemented widely in practise since 1960s. Utilizing the divided and conquer, QuickSort gains good performance by choose one pivot to seperate the input array into two parts (one larger than pivot and another is smaller than pivot) in each iteration. It was thought that one pivot scheme was better than the multiple pivot scheme until dual pivot was proved better by implementation [2] in 2009. Then, 3-pivot QuickSort algorithm [3] was put up by introducing a smart way to swap the elements. In this report, we will explain and implement QuickSort, 2-pivot QuickSort and 3-pivot QuickSort. Through the experiment, we try to show the gains of more pivot. We will also try to get some insights. Finally, we will explore the impact of data pattern (many duplicate elements or almost sorted) on the algorithm.

[1] Charles AR Hoare. Quicksort.The Computer Journal, 5(1):10–16, 1962.

[2] Vladimir Yaroslavskiy. Dual-pivot quicksort.Research Disclosure, 2009.

[3] Shrinu Kushagra, Alejandro L ́opez-Ortiz, J Ian Munro, and Aurick Qiao.Multi-pivot quicksort: Theory and experiments. InProceedings of the Meet-ing on Algorithm Engineering & Expermiments, pages 47–60. Society forIndustrial and Applied Mathematics, 2014.
