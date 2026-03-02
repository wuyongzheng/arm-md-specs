## B1.1 Overview

- The RMM exposes the following interfaces to the Host:
- The Realm Management Interface (RMI)
- The RMM exposes the following interfaces to a Realm:
- The Realm Services Interface (RSI)
- The Power State Coordination Interface (PSCI)

Any other SMC executed by a Realm returns SMCCC\_NOT\_SUPPORTED.

- An RMM interface consists of a set of RMM commands.
- An RMM interface is compliant with the SMC Calling Convention (SMCCC).
- SMCCC version &gt;= 1.2 is required.
- SMCCC version 1.2 increases the number of SMC64 arguments and return values from 4 to 17. Some RMM commands use more than 4 input or output values.
- On a CCA platform which implements FEAT\_SVE, SMCCC version &gt;= 1.3 is required.
- SMCCC version 1.3 introduces a bit in the FID which a caller can use to indicate that SVE state does not need to be preserved across the SMC call.
- On a CCA platform which implements FEAT\_SME, SMCCC version &gt;= 1.4 is required.
- SMCCC version 1.4 adds support for preservation of SME state across an SMC call.
- An RMM command uses the SMC64 calling convention.
- To determine whether an RMM interface is implemented, software should use the following flow:
1. Determine whether the SMCCC\_VERSION command is implemented, following the procedure described in Arm SMC Calling Convention [23].
2. Check that the SMCCC version is &gt;= 1.1.
3. Execute the &lt;Interface&gt;.Version command, which returns:
- SMCCC\_NOT\_SUPPORTED (-1) if &lt;Interface&gt; is not implemented.


- A version number (&gt;0) if &lt;Interface&gt; is implemented.
- All data types defined in this specification are little-endian.

See also:

- Chapter B4 Realm Management Interface
- Chapter B5 Realm Services Interface
- Chapter B6 Power State Control Interface