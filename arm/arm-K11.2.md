## K11.2 Load-Acquire, Store-Release and barriers

The Load-Acquire and Store-Release instructions are described in Load-Acquire, Load-AcquirePC, and Store-Release.

## K11.2.1 Message passing

The following sections describe:

- Resolving weakly-ordered message passing by using Acquire and Release.
- Resolving message passing by the use of Store-Release and address dependency.

## K11.2.1.1 Resolving weakly-ordered message passing by using Acquire and Release

Weakly-ordered message passing can be solved by the use of Load-Acquire and Store-Release instructions when accessing the communications flag:

AArch32

P1

STR R5, [R1]

STL R0, [R2]

WAIT\_ACQ([R2]==1)

LDR R5, [R1]

AArch64

P1

STR W5, [X1]

STLR W0, [X2]

; sets new data

; sends flag indicating data ready, which is ordered after the STR

; waits on flag

; sets new data

; sends flag indicating data ready, which is ordered after the STR

WAIT\_ACQ([X2]==1) ; waits on flag LDR W5, [X1]

This ensures the observed order of both the reads and the writes allows transfer of data such that the result P2:R5== 0x55 is guaranteed.

This approach also works with multiple observers, in a way that further observers use the same sequence as P2 uses:

AArch32

P3

WAIT\_ACQ([R2]==1)

; waits on flag

LDR R5, [R1]

AArch64

P3

WAIT\_ACQ([X2]==1) ; waits on flag LDR W5, [X1]

## K11.2.1.2 Resolving message passing by the use of Store-Release and address dependency

Where the ordering of Normal memory accesses is not resolved by the use of barriers or dependencies, then different observers might observe the accesses in a different order. This can be resolved by the use of Store-Release for the store of the valid flag by P1, even when the observers are using an address dependency:

AArch32

P1

P2

P2

## P2

```
WAIT([R2]==1) AND R12, R12, #0 ; R12 is the destination of LDR in the WAIT LDR R5, [R1, R12] ; the load has an address dependency on R12 : and so is ordered after the flag has been seen
```

## AArch64

## P1

STR W5, [X1]

; sets new data

STLR W0, [X2]

; sends flag indicating data ready using a Store-Release

```
WAIT([X2]==1) AND W12, W12, WZR ; W12 is the destination of LDR in the WAIT LDR W5, [X1, X12] ; the load has an address dependency on W12
```

macro

: and so is ordered after the flag has been seen

This ensures the observed order of the writes allows transfer of data such that P2:R5 and P3:R5 contain the same value of 0x55 .

This approach also works with multiple observers, in a way that further observers use the same sequence as P2 uses:

AArch32

## P3

```
WAIT([R2]==1) AND R12, R12, #0 ; R12 is the destination of LDR in the WAIT LDR R5, [R1, R12] ; the load has an address dependency on R12 : and so is ordered after the flag has been seen
```

```
AArch64 P3
```

```
WAIT([X2]==1) AND W12, W12, WZR ; R12 is the destination of LDR in the WAIT LDR W5, [X1, X12] ; the load has an address dependency on W12 : and so is ordered after the flag has been seen
```

## K11.2.2 Address dependency with object construction

When accessing an object-oriented data structure, the address dependency rule means that barriers are not required, even when initializing the object. A Store-Release can be used to ensure the order of the update of the base address:

AArch32

## P1

```
STR R5, [R1, #offset] ; sets new data in a field STL R1, [R2] ; updates base address
```

```
LDR R1, [R2] ; reads base address CMP R1, #0 ; checks if it is valid BEQ null_trap LDR R5, [R1, #offset] ; uses base address to read field
```

## P2

## P2

```
STR R5, [R1] ; sets new data STL R0, [R2] ; sends flag indicating data ready using a Store-Release
```

macro

```
macro
```

```
macro
```

AArch64

## P1

```
STR W5, [X1, #offset] ; sets new data in a field STLR X1, [X2] ; updates base address
```

```
LDR X1, [X2] ; reads base address CMP X1, #0 ; check if it is valid B.EQ null_trap LDR W5, [X1, #offset] ; uses base address to read field
```

It is required that P2:R5== 0x55 if the null\_trap is not taken. This avoids P2 observing a partially constructed object from P1. Significantly, P2 does not need a barrier to ensure this behavior.

The read of the base address in P2 could be a Load-Acquire, but it is not necessary in this case.

## P2