## D20.1 About the RAS Extension

ILBKPL

The RAS Extension extends the exception syndrome registers to include fields that allow the PE to report a PE error state when an Error exception is taken.

ITHGHB

RYWXWL

The RAS Extension defines System registers that are specific to RAS, including to access optional Error records defined by the RAS System Architecture. The format of the error record registers is defined in Error record System register view.

The RAS Extension does not prescribe the level of reliability, availability, and serviceability in the PE. The RAS features that the system and PE include, for example to detect, correct, contain, or defer errors, are IMPLEMENTATION DEFINED. The RAS Extension defines a framework for building RAS features in a PE.

## Example D20-1 Minimal implementation of RAS Extension

For systems without a requirement for high reliability and availability, a minimal approach to RAS might include:

- There is no error detection. ERRIDR\_EL1.NUM is zero, indicating that no error records are implemented. See Error record System register view.
- Any error signaled to the PE generates an asynchronous SError exception, and on taking the SError exception:
- -The PE error state is recorded as Uncontainable (UC).
- -If FEAT\_RASv2 is implemented, then ESR\_ELx.VFV is set to 0, meaning FAR\_ELx is UNKNOWN and not valid. If FEAT\_RASv2 is not implemented, then FAR\_ELx is always UNKNOWN and not valid on taking an SError exception.
- -
- FEAT\_PFAR is not implemented, meaning ESR\_ELx.PFV is set to 0.

See Taking error exceptions.

- The ESB instruction is implemented as NOP .

See also ESB and virtual SError exceptions and ESB and delegated SError exceptions.

## Example D20-2 Minimal implementation of RAS Extension

For systems without a requirement for high reliability and availability, a minimal approach to RAS might include:

- There is no error detection. ERRIDR\_EL1.NUM is zero, indicating that no error records are implemented. See Error record System register view.
- Any error signaled to the PE generates an asynchronous SError exception, and on taking the SError exception the PE error state is recorded as Uncontainable (UC). See Taking error exceptions.
- The ESB instruction is implemented as NOP . See also ESB and virtual SError exceptions and ESB and delegated SError exceptions.

## Example D20-3 Common error handling for RAS features

For a system with a requirement for high reliability and error containment:

- When errors are detected, they are recorded in error records. This includes both correctable and uncorrectable errors. Error correction and detection logic exists on all significant memory structures, and might include other non-memory structures.
- Most uncorrectable errors generate poison values to defer the error.
- On consuming poison from the memory system, a load instruction that would corrupt PE state generates a synchronous External Abort exception, regardless of the memory type. For systems where the performance impact of this approach might be an issue, the controls defined by FEAT\_ANERR and FEAT\_ADERR are provided.
- On taking error exceptions, the PE error state is Recoverable state (UER).
- FEAT\_PFARis implemented, and the PE makes a best effort attempt to record the faulting physical address in PFAR\_ELx or MFAR\_ELx, setting ESR\_ELx.PFV to 1.

IQGLBZ

See also Arm ® Reliability Availability and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100) for more information about the framework for building RAS features in a system.