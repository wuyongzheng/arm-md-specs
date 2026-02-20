## D7.6 External aborts

The Arm architecture defines External aborts as errors that occur in the memory system, other than those that are detected by the MMU or debug logic. An External abort might signal a data corruption to the PE. For example, a memory location might have been corrupted, and this corruption is detected by hardware using a parity or error correction code (ECC). The error might have been propagated. The RAS Extension provides mechanisms for software to determine the extent of the corruption and contain propagation of the error. For more information, see RAS PE Architecture.

An External abort is one of the following:

- Synchronous.
- Precise asynchronous.
- Imprecise asynchronous.

For more information, see Exception entry terminology.

The RAS Extension provides a more granular taxonomy of aborts. When the RAS Extension is not implemented, the Arm architecture does not provide any method to distinguish between precise asynchronous and imprecise asynchronous External aborts.

It is IMPLEMENTATION DEFINED which External aborts, if any, are supported.

External aborts on data accesses and translation table walks on data accesses can be either synchronous or asynchronous.

When FEAT\_DoubleFault is not implemented, External aborts on instruction fetches and translation table walks on instruction fetches can be either synchronous or asynchronous.

When FEAT\_DoubleFault is implemented, all External abort exceptions on instruction fetches and translation table walks on instruction fetches must be synchronous.

Asynchronous External abort on an instruction fetch, including a translation table walk on an instruction fetch, is taken precisely using the Instruction Abort exception.

Asynchronous External abort on a data read or write, including a translation table walk on a data read or write, is taken precisely using the Data Abort exception.

See Synchronous exception types.

An asynchronous External abort is taken using the SError exception. See Asynchronous exception types.

The effect of a failed memory access is described in Definition of a precise exception and imprecise exception.

Normally, External aborts are rare. An imprecise asynchronous External abort is likely to be fatal to the process that is running, Arm recommends that implementations make External aborts precise wherever possible.

The following subsections give more information about possible External aborts:

- Provision for the classification of External aborts.
- Parity or ECC error reporting, RAS Extension not implemented.

## D7.6.1 Provision for the classification of External aborts

In AArch64 state, an implementation can use ESR\_ELx.EA, ISS[9], to provide more information about synchronous External aborts. For all synchronous aborts other than synchronous External aborts, ESR\_ELx.EA, ISS[9], returns a value of 0.

If the FEAT\_RAS is implemented:

- The ESR\_ELx.SET field provides information about the state of the PE following a synchronous External abort.
- The ESR\_ELx.AET field might contain more information following an asynchronous abort taken as an SError exception.
- The implementation might define error record registers.

For more information, see:

- ISS encoding for an exception from an Instruction Abort.
- ISS encoding for an exception from a Data Abort.
- ISS encoding for an SError exception.
- Taking error exceptions.

## D7.6.2 Parity or ECC error reporting, RAS Extension not implemented

The Arm architecture supports the reporting of both synchronous and asynchronous parity or ECC errors from the cache system. It is IMPLEMENTATION DEFINED what parity or ECC errors in the cache systems, if any, result in synchronous or asynchronous parity or ECC errors.

Afault code is defined for reporting parity or ECC errors. However, when parity or ECC error reporting is implemented, it is IMPLEMENTATION DEFINED whether a parity or ECC error is reported using the assigned fault code or using another appropriate encoding.

For all purposes other than the Fault status encoding, parity or ECC errors are treated as External aborts.