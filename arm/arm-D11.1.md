## D11.1 Introduction

## D11.1.1 Protection for return addresses

INTVZJ

Return oriented programming (ROP) is a common method used by attackers to execute code in a way that was not intended and to bypass security defenses. ROP techniques involve changing the return address of procedure calls to cause execution to change to a different path. Since the return address of procedures is often stored on the stack, once an attacker has basic write capabilities to data memory, it has the ability to change the return addresses. Technologies such as Pointer Authentication help to significantly reduce the scope of an attack and the scenarios in which attacks are possible.

GHMVDQ

To further improve the integrity of return addresses, the Guarded Control Stack provides means to securely store return addresses such that they are immutable, and provides means to check a return address has not been compromised.

## D11.1.2 Call stack recording

IZHHFX

Ahistory of the call stack provides useful information when debugging or optimizing a program. Typically, the call stack is collected at important points by unwinding the stack to collect the return address stored in each frame. This unwinding procedure can be intrusive or impractical, due to the need to analyze large amounts of memory and because the stack frames are variable in size, although some of this is mitigated by the use of frame pointers. Providing the call stack in a format which is simpler to extract at run time can substantially reduce the cost of collecting the call stack, and make new usage models possible.

GHXYWV

To reduce the costs of collecting the call stack information, the Guarded Control Stack provides means to automatically collect return addresses in easily accessible memory.

## D11.1.3 Overview

| I VCTSV   | The Guarded Control Stack protects against use of procedure return instructions to return anywhere other than the return address created when the procedure was called.                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I CQCMQ   | Optionally, the Guarded Control Stack protection of procedure return instructions does not require the instruction sequences for function calls, prologues, or epilogues to be modified.                                                                                                                                 |
| I DMTVT   | The Guarded Control Stack provides protection against using exception return instructions to return anywhere other than the intended return address, for exceptions taken within the same Exception level.                                                                                                               |
| I HPDGB   | The Guarded Control Stack provides the ability to capture the call stack for multiple concurrent applications.                                                                                                                                                                                                           |
| I YYFJV   | The contents of the Guarded Control Stack are immutable to software running at the same Exception level, unless explicitly permitted by a higher Exception level.                                                                                                                                                        |
| I TGPWS   | The contents of the Guarded Control Stack are readable to software running at the same Exception level.                                                                                                                                                                                                                  |
| I JGNWV   | The management of the Guarded Control Stack does not require a call to privileged code when using various performance critical user space software constructs which manipulate the main stack or switch between multiple stacks. Such software constructs include soft exceptions, setjmp/longjmp, and software threads. |
| I DLBKT   | The Guarded Control Stack supports protection and recording in AArch64 state.                                                                                                                                                                                                                                            |
| I JXYXZ   | The Guarded Control Stack is not supported in AArch32 state.                                                                                                                                                                                                                                                             |
| I LFRDH   | The Guarded Control Stack supports capturing the call stack for kernel and user space software independently.                                                                                                                                                                                                            |
| I KLBVV   | When switching between stacks within an Exception level, FEAT_GCS provides the ability to switch between different Guarded Control Stacks without affecting the immutability of any of the Guarded Control Stacks.                                                                                                       |