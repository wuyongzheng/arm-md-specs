## K11.1 Introduction

The exact rules for the insertion of barriers into code sequences is a complicated subject, and this appendix describes many of the corner cases and behaviors that are possible in an implementation of the Arm architecture.

This appendix is to help programmers, hardware design engineers, and validation engineers understand the need for the different kinds of barriers.

## K11.1.1 Overview of memory consistency

Early generations of microprocessors were relatively simple processing engines that executed each instruction in program order. In such processors, the effective behavior was that each instruction was executed in its entirety before a subsequent instruction started to be executed. This behavior is sometimes referred to as the Sequential Execution Model (SEM), and in this Manual it is described as Simple sequential execution of the program.

In later processor generations, the needs to increase processor performance, both in terms of the frequency of operation and the number of instructions executed each cycle, mean that such a simple form of execution is abandoned. Many techniques, such as pipelining, write buffering, caching, speculation, and out-of-order execution, are introduced to provide improved performance.

For general-purpose PEs, such as Arm, these microarchitectural innovations are largely hidden from the programmer by a number of microarchitectural techniques. These techniques ensure that, within an individual PE, the behavior of the PE largely remains the same as the SEM. There are some exceptions to this where explicit synchronization is required. In the Arm architecture, these are limited to cases such as:

- Synchronization of changes to the instruction stream.
- Synchronization of changes to System registers.

In both these cases, the ISB instruction provides the necessary synchronization.

While the effect of ordering is largely hidden from the programmer within a single PE, the microarchitectural innovations have a profound impact on the ordering of memory accesses. Write buffering, speculation, and cache coherency protocols, in particular, can all mean that the order in which memory accesses occur, as seen by an external observer, differs significantly from the order of accesses that would appear in the SEM. This is usually invisible in a uniprocessor environment, but the effect becomes much more significant when multiple PEs are trying to communicate with memory. In reality, these effects are often only significant at particular synchronization boundaries between the different threads of execution.

The problems that arise from memory ordering considerations are sometimes described as the problem of memory consistency . Processor architectures have adopted one or more memory consistency models , or memory models , that describe the permitted limits of the memory reordering that can be performed by an implementation of the architecture. The comparison and categorization of these has generated significant research and comment in academic circles, and Arm recommends the Memory Consistency Models for Shared Memory-Multiprocessors paper as an excellent detailed treatment of this subject.

This appendix does not reproduce such a work, but instead concentrates on some cases that demonstrate the features of the weakly-ordered memory model of the Arm architecture from Armv6. In particular, the examples show how the use of the DMB and DSB memory barrier instructions can provide the necessary safeguards to limit memory ordering effects at the required synchronization points.

## K11.1.2 Barrier operation definitions

The following reference, or provide, definitions of terms used in this appendix:

DMB

See Data Memory Barrier.

DSB

See Data Synchronization Barrier.

ISB

See Instruction Synchronization Barrier.

Observer, Completion

See Ordering requirements defined by the formal concurrency model.

See Completion and endpoint ordering.

## Program order

## K11.1.3 Conventions

Many of the examples are written in a stylized extension to Arm assembler, to avoid confusing the examples with unnecessary code sequences.

AArch32

The construct WAIT([Rx]==1) describes the following sequence:

```
R12, [Rx]
```

```
loop LDR CMP R12, #1 BNE loop
```

Also, the construct WAIT\_ACQ([Rx]==1) describes the following sequence:

```
loop LDA R12, [Rx] ; load acquire ensures it is ordered before subsequent loads/stores CMP R12, #1 BNE loop
```

R12 is chosen as an arbitrary temporary register that is not in use. It is named to permit the generation of a false dependency to ensure ordering.

AArch64

The construct WAIT([Xx]==1) describes the following sequence:

```
W12, [Xx]
```

```
loop LDR CMP W12, #1 B.NE loop
```

Also, the construct WAIT\_ACQ([Xx]==1) and describes the following sequence:

```
loop LDAR W12, [Xx] ; load acquire ensures it is ordered before subsequent loads/stores CMP W12, #1 B.NE loop
```

For each example, a code sequence is preceded by an identifier of the observer running it:

- P0, P1 . . . P x refer to caching coherent PEs that implement the Armv9 or Armv8 architecture and are in the same shareability domain.
- E0, E1 . . . E x refer to non-caching observers that do not participate in the coherency protocol, but execute Armv9 or Armv8 instructions and have a weakly ordered memory model. This does not preclude these observers being different objects, such as DMA engines or other system Requesters.

These observers are unsynchronized other than as required by the documented code sequence.

Note

Throughout this appendix, Armv9 or Armv8 instruction and instruction refer to instructions from the A64, A32, or T32 instruction set, provided by Armv9 or Armv8 implementations.

Results are expressed in terms of &lt;agent&gt;:&lt;register&gt; , such as P0:R5 . The results can be described as:

The order of instructions as they appear in an assembly language program. This appendix does not attempt to describe or define the legal transformations from a program written in a higher-level programming language, such as C or C++, into the machine language that can then be disassembled to give an equivalent assembly language program. Such transformations are a function of the semantics of the higher-level language and the capabilities and options on the compiler.

Permissible

Not permissible

This does not imply that the results expressed are required or are the only possible results. In most cases they are results that would not be possible under a sequentially consistent running of the code sequences on the agents involved. In general terms, this means that these results might be unexpected to anyone unfamiliar with memory consistency issues.

Results that the architecture expressly forbids.

Required Results that the architecture expressly requires.

The examples omit the required shareability domain arguments of DMB and DSB instructions. The arguments are assumed to be selected appropriately for the shareability domains of the observers.

In AArch32 state, where the barrier function in the litmus test can be achieved by a DMB ST , that is a barrier to stores only, this is shown by the use of DMB [ST] . This indicates that the ST qualifier can be omitted without affecting the result of the test. In some implementations DMB ST is faster than DMB .

For AArch64 code, the shareability domain of the DMB or DSB must be included. This is shown in this manual using the notation DMB &lt;domain&gt; and DSB &lt;domain&gt; respectively.

Except where otherwise stated, other conventions are:

- All memory initializes to 0.
- R0 and W0 contain the value 1.
- R1 - R4 and W1 - W4 contain arbitrary independent addresses that initialize to the same value on all PEs. The addresses held in these registers are shareable and:
- -The addresses held in R1 and R2 are in Write-Back Cacheable Normal memory.
- -The address held in R3 is in Write-Through Cacheable Normal memory.
- -The address held in R4 is in Non-cacheable Normal memory.
- R5 - R8 and W5 - W8 contain:
- -When used with an STR instruction, 0x55 , 0x66 , 0x77 , and 0x88 respectively.
- -When used with an LDR instruction, the value 0.
- R11 and W11 contain a new instruction or new translation table entry, as appropriate, and R10 contains the virtual address and the ASID, for use in this change of translation table entry.
- Memory locations are Normal memory locations unless otherwise stated.

The examples use mnemonics for the cache maintenance and TLB maintenance instructions. The following tables describe the mnemonics:

- Cache maintenance system instructions.
- TLB maintenance system instructions.