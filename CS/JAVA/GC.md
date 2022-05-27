GC
===
> JVM에서 더 이상 사용되지 않는 데이터가 할당되어 있는 메모리 공간을 해제 시켜주는 장치
+ Stop-The-World - GC가 발생할시 GC를 담당하는 Thread를 제외한 모든 Thread가 일시적으로 정지할 때.
+ Mark - 애플리케이션이 일시 중시될시 GC는 참조되는 객체와 연결된 객체를 타고 이동하며 접근 가능한 객체를 식별하는 작업.
+ Sweep - 객체 탐색이 끝나면, Mark되지 않은 객체들을 메모리에서 해제시키는 작업.

#### 장점
+ 개발자가 동적으로 할당된 메모리 전체를 관리할 필요가 없다.
+ 유효하지 않은 포인터에 접근 혹은 한번 해제한 메모리를 두번 해제하는 등의 버그나 불필요 작업을 최소화 할수 있음.
#### 단점
+ GC가 발생하는 정확한 시점을 개발자 입장에서 알 수가 없기에 예측 불가하게 Stop-the-World가 발생하여 프로그램이 멈추는 상황이 발생하기에, 실시간 시스템에 적합하지 않다.
+ 개발자의 실수등을 통하여 객체를 참조할 수 있는 경로가 존재시, 사용가능성이 존재하기에 GC가 메모리를 해제하지 않는 경우가 생김.

### GC의 메모리 해제 판단 기준
![GC_Memory](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fp0fV4%2Fbtq52U1JmsB%2FyqeiJPbptaqHMbrTl3r85K%2Fimg.png)

+ 참조하는 회수가 0회가 될 시
  + 상호 참조 관계시 GC 판단기준에 부적합하게 되어 메모리의 누수가 발생할 가능성이 존재.
+ 참조하는 경로가 없어 질 시
### Minor GC
> Heap의 Yonung영역에 GC가 발생할경우.

Survivor1/2 swapping하며 Clear, Survivor 영역에서 오래 살아남을시 Old영역으로 이동.
![Minor_GC_flow](https://mirinae312.github.io/img/jvm_gc/JVMObjectLifecycle.png)
### Major GC
> Old Generation의 메모리도 충분하지 않으면, 해당 영역에도 GC가 발생하는 경우.

### Serial GC
> 가장 단순한 GC로, 싱글 쓰레드로 동작하며 다른 GC에 비하여 Stop the World의 시간이 긺.  
> Mark sweep Compact 알고리즘을 사용한다.
> 

### Parallel GC
> Java 8의 default GC이며 Young영역의 GC를 멀티쓰레드로 진행함.
> 
![Parallel GC](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLt8SI%2FbtqZpUghb6U%2FbWL987lUHZTGe51qHfoOVk%2Fimg.png)
### Parallel Old GC
> Parallel GC에서 Old영역까지 멀티쓰레드를 확장한 GC.
> 
### CMS GC
> `Stop the World`로 자바 애플리케이션이 멈추는 현상을 해결하고자 만들어진 GC로 4스텝에 걸쳐 나눠지는 방법을 채택.
> 
![Concurrent_mark_sweep_GC](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FchM1aO%2FbtqZtAafO9I%2Fx5ieeSoLcjfbMftBS6pkLK%2Fimg.png)
1. Initial Mark - 클래스 로더에서 가장 가까운 살아있는 객체만 찾음.(stop the world가 발생하나, 멈추는 시간이 매우 짧음.)
2. Concurrent Mark - Initial Mark한 객체에서 참조하고 있는 객체를 따라가며 확인. 다른 쓰레드가 실행중인상태에서 동시에 진행되는 특징을 가짐.
3. Remark - Concurrent Mark단계에서 새로 추가되거나 참조가 끊긴 객체를 확인.(stop the world 발생)
4. Concurrent Sweep - 접근 불가한 객체를 삭제 작업 진행, 다른 쓰레드가 실행중인 상태에서 동시에 진행.
### G1 GC
> Java 9의 default GC이며, 현재 나온 STW 시간이 GC에서 가장 시간이 짧음.

기존 힙메모리와는 달리, 전체 힙메모리를 Region이라는 특정한 크기로 나눠서 각 Region status에 따라서 그 Region(Eden,Survivor,Old)에 역할이 동적으로 부여되는 상태로 존재한다.  
추가적으로, Humongous, Available/Unused 이 존재하며 두 Region에 대한 역할은 아래와 같다.

Humongous : Region 크기의 50%를 초과하는 큰 객체를 저장하기 위한 공간이며, 이 Region 에서는 GC 동작이 최적으로 동작하지 않는다.

Available/Unused : 아직 사용되지 않은 Region을 의미한다.
G1 GC에서 Young GC 를 수행할 때는 STW(Stop-The-World) 현상이 발생하며, STW 시간을 최대한 줄이기 위해 멀티스레드로 GC를 수행한다. Young GC는 각 Region 중 GC대상 객체가 가장 많은 Region(Eden 또는 Survivor 역할) 에서 수행 되며, 이 Region 에서 살아남은 객체를 다른 Region(Survivor 역할) 으로 옮긴 후, 비워진 Region을 사용가능한 Region으로 돌리는 형태 로 동작한다.

1. Initial Mark - Old Region 에 존재하는 객체들이 참조하는 Survivor Region 을 찾는다. 이 과정에서는 STW 현상이 발생하게 된ㄷ.
2. Root Region Scan - Initial Mark 에서 찾은 Survivor Region에 대한 GC 대상 객체 스캔 작업을 진행한다.
3. Concurrent Mark - 전체 힙의 Region에 대해 스캔 작업을 진행하며, GC 대상 객체가 발견되지 않은 Region 은 이후 단계를 처리하는데 제외되도록 한다.
4. Remark - 애플리케이션을 멈추고(STW) 최종적으로 GC 대상에서 제외될 객체(살아남을 객체)를 식별해낸다.
5. Cleanup - 애플리케이션을 멈추고(STW) 살아있는 객체가 가장 적은 Region 에 대한 미사용 객체 제거 수행한다. 이후 STW를 끝내고, 앞선 GC 과정에서 완전히 비워진 Region 을 Freelist에 추가하여 재사용될 수 있게 한다.
6. Copy - GC 대상 Region이었지만 Cleanup 과정에서 완전히 비워지지 않은 Region의 살아남은 객체들을 새로운(Available/Unused) Region 에 복사하여 Compaction 작업을 수행한다.
![Mark_and_swwep](https://mirinae312.github.io/img/jvm_gc/MarkSweepCompaction.png)