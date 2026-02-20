## D2.10 Vector Catch exceptions

Vector Catch exceptions are not generated in AArch64 translation regimes.

Note

This means that they are never taken to EL1 using AArch64 and are supported only if at least EL1 using AArch32 is supported.

Adebugger that is executing in EL2 using AArch64 can route Vector Catch exceptions to EL2 using AArch64. See Routing debug exceptions.

AArch64.VectorCatchException() is called to generate a Vector Catch exception.

Vector Catch exceptions describes Vector Catch exceptions.