## D2.6 Pseudocode description of debug exceptions

The AArch64.Abort() function processes FaultRecord objects, as described in Abort exceptions, and generates a debug exception.

Some functions called by AArch64.Abort() are:

- AArch64.BreakpointException() .
- AArch64.WatchpointException() .
- AArch64.VectorCatchException() .
- AArch64.InstructionAbort() .
- AArch64.DataAbort() .

These functions are defined in A-profile Architecture Pseudocode.