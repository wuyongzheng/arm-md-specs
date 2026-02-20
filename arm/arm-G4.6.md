## G4.6 External aborts

The Arm architecture defines External aborts as errors that occur in the memory system, other than those that are detected by the MMU or Debug hardware. An External abort might signal a data corruption to the PE. For example, a memory location might have been corrupted, and this corruption is detected by hardware using a parity or error correction code (ECC). The error might have been propagated. The RAS Extension provides mechanisms for software to determine the extent of the corruption and contain propagation of the error. For more information, see RAS PE Architecture.

An External abort is one of:

- Synchronous.
- Precise asynchronous.
- Imprecise asynchronous.

For more information, see Exception terminology.

The RAS Extension provides an expanded taxonomy for describing aborts. When the RAS Extension is not implemented, the Arm architecture does not provide any method to distinguish between precise asynchronous and imprecise asynchronous External aborts.

VMSAv8-32 permits External aborts on data accesses, translation table walks, and instruction fetches to be either synchronous or asynchronous. The reported fault code identifies whether the External abort is synchronous or asynchronous.

It is IMPLEMENTATION DEFINED which External aborts, if any, are supported. Asynchronous External aborts generate SError exceptions.

In AArch32 state:

- SError exceptions are taken as asynchronous Data Abort exceptions.
- Synchronous External aborts:
- -On data accesses are taken as synchronous Data Abort exceptions.
- -On instruction fetches, or prefetches, are taken as synchronous Prefetch Abort exceptions.

See also:

- External abort on a translation table walk.
- Handling exceptions that are taken to an Exception level using AArch32.

Normally, External aborts are rare. An imprecise asynchronous External abort is likely to be fatal to the process that is running. Arm recommends that implementations make External aborts precise wherever possible.

The following subsections give more information about possible External aborts:

- Provision for classification of External aborts.
- Parity or ECC error reporting, FEAT\_RAS not implemented.

The section Exception reporting in a VMSAv8-32 implementation describes the reporting of External aborts.

## G4.6.1 Provision for classification of External aborts

For an External abort taken to a privileged mode other than Hyp mode, an implementation can use the DFSR.ExT or IFSR.ExT bits to provide more information about the External abort:

- DFSR.ExT provides an IMPLEMENTATION DEFINED classification of External aborts on data accesses.
- IFSR.ExT provides an IMPLEMENTATION DEFINED classification of External aborts on instruction accesses.

For an External abort taken to Hyp mode, the HSR.EA bit, provides an IMPLEMENTATION DEFINED classification of External aborts.

For all aborts other than External aborts these bits return a value of 0.

If the FEAT\_RAS is implemented:

- The HSR.AET field provides information about the state of the PE following an SError exception taken to Hyp mode.
- The DFSR.AET field provides information about the state of the PE following an asynchronous Data Abort exception.
- The implementation might define error record registers.
- DFSR.{AET, ExT} is set to values from VDFSR or VSESR\_EL2 in the case of a virtual SError exception.

For more information on the RAS Extension, see RAS PE Architecture.

## G4.6.2 Parity or ECC error reporting, FEAT\_RAS not implemented

The Arm architecture supports the reporting of both synchronous and asynchronous parity or ECC errors from the cache systems. It is IMPLEMENTATION DEFINED what parity or ECC errors in the cache systems, if any, result in synchronous or asynchronous parity or ECC errors.

Afault code is defined for reporting parity or ECC errors, see Exception reporting in a VMSAv8-32 implementation. However when parity or ECC error reporting is implemented it is IMPLEMENTATION DEFINED whether a parity or ECC error is reported using the assigned fault code, or using another appropriate encoding.

For all purposes other than the Fault status encoding, parity or ECC errors are treated as External aborts.