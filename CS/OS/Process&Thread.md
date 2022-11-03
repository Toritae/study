Process & Thread
===
Process
---
> 컴퓨터에서 '연속적'으로 실행되고 있는 프로그램 or 메모리에 적재되 실행되고 있는 프로그램의 '인스턴스'
> 
### 특징
1. 각 프로세스는 시스템으로부터 독립된 메모리 영역(Stack, Heap, data, code)을 할당받는다.  
2. 기본적으로 한 프로세스는 최소 하나의 Thread를 보유하고있다.
3. 프로세스가 타 프로세스 영역의 자원을 참조하려고 한다면, 프로세스간의 통신이 필요하다.(IPC, inter-process community)
    + 파일, 소켓, 파이프등의 통신

Thread
---
> '한'프로세스내에서 실행되는 흐름의 단위.

### 특징
1. 각 Thread는 code, data, heap 영역을 공유하며, Stack 영역은 개별로 할당 받는다.  
2. 즉, code, data, heap 영역을 공유하고 있기에, context switching의 비용이 프로세스보다 적은 장점을 가지고있다.



Multi Processing
---
> 하나의 응용프로그램을 여러개의 프로세스로 구성하여 하나의 응용프로그램을 처리 하도록 하는 기법.
> 
### 특징
1. 

Multi Threading
---