## D8.10 Pointer authentication

| I XDNDT   | AArch64 state supports signing the contents of a 64-bit general-purpose register that contains an address with a pointer authentication code (PAC), and authenticating the contents of a register with a PAC before the register is used as the target of an indirect branch, or the base register of a load or store instruction.   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R STHJF   | All statements in this section and subsections require implementation of FEAT_PAuth.                                                                                                                                                                                                                                                 |
| R JZTGK   | Pointer authentication is supported only in AArch64 state.                                                                                                                                                                                                                                                                           |
| I PKPFN   | If Pointer authentication is implemented, then both of the following are true:                                                                                                                                                                                                                                                       |
| I GMTCR   | Pointer authentication functionality is the same whether address translation is enabled or disabled, but is useful only when address translation is enabled.                                                                                                                                                                         |

## D8.10.1 PAC field

IKQZPC

The pointer authentication mechanism treats the upper bits of a pointer in a 64-bit general-purpose register as a PAC field.

IBSXBR

The TCR\_ELx.{T0SZ, T1SZ} fields are used to configure the size and location of the PAC field.

RFWYCF

If FEAT\_CONSTPACFIELD is not implemented, when a 64-bit general-purpose register, Xd, holds an address with a PAC field, the location of the PAC field is determined by all of the following:

- The bottom\_PAC\_bit is 64-TCR\_ELx.T n SZ, and the value of n is determined as follows:
- -If inserting a PAC into an address and address tagging is not used, then the value of Xd[63] is the value of n .
- -Otherwise, the value of Xd[55] is the value of n .
- If address tagging is used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[55: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[54: bottom\_PAC\_bit ].
- If address tagging is not used and logical address tagging is used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[63:60, 55: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[63:60, 54: bottom\_PAC\_bit ].
- If both address tagging and logical address tagging are not used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[63: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[63:56, 54: bottom\_PAC\_bit ].

For more information, see Address tagging and Logical Address Tagging.

Note

ATCR\_ELx.T n SZ value less than 12 requires implementation of FEAT\_LV A3.

If FEAT\_LVA3 is implemented, and address tagging or logical address tagging are enabled, pointer authentication might provide software with little to no benefit due to the reduced PAC field size.

If FEAT\_CONSTPACFIELD is implemented, when a 64-bit general-purpose register, Xd, holds an address, the location of the PAC field is determined by all of the following:

- The bottom\_PAC\_bit is 64-TCR\_ELx.T n SZ.
- The value of Xd[55] is the value of n used in T n SZ.

RXTGWV

RNQZWG

IVZRCW

IHLQVM

- If address tagging is used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[55: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[54: bottom\_PAC\_bit ].
- If address tagging is not used and logical address tagging is used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[63:60, 55: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[63:60, 54: bottom\_PAC\_bit ].
- If both address tagging and logical address tagging are not used, then all of the following apply:
- -If bottom\_PAC\_bit is &gt; 52 and the stage 1 translation supports a single V A range, then the PAC field is Xd[63: bottom\_PAC\_bit ].
- -Otherwise, the PAC field is Xd[63:56, 54: bottom\_PAC\_bit ].

If FEAT\_CONSTPACFIELD is implemented, then an implementation is permitted to use the value in Xd[55] to determine the size of the PAC field when adding a PAC to Xd, even when address tagging is not used.

In the case where address tagging is not used, then any use of a V A that has differing values of bit [63] and bit [55] is a non-canonical VA that will generate a fault. For this reason, the presence or absence of FEAT\_CONSTPACFIELD does not affect the use of pointer authentication when inserting a PAC into a canonical V A.

If the TCR\_ELx.TBID{ n } bit is used to restrict address tagging to data addresses, then instruction addresses can use Xd[63:56] bits to produce larger pointer authentication code fields.

IDJNGK For all of the following reasons, if FEAT\_PAuth2 is implemented, FEAT\_FPAC is not implemented, and stage 1 translation is disabled, then Arm recommends not setting the TCR\_ELx.T n SZ values to indicate an address range that is smaller than the PA size:

- For some PAC values, if TCR\_ELx.T n SZ is set to indicate an address range that is smaller than the PA size, the address generated by a failed PAC authentication might be an address within the PA size because the upper address bits, those between the PA size and the size indicated by the TCR\_ELx.T n SZ field, are taken from the result of the authentication process.
- Accessing memory using such an address that has failed PAC authentication does not generate an Address size fault.
- The memory access is done using upper address bits, those between the PA size and the size indicated by the TCR\_ELx.T n SZ field, taken from the result of the authentication process.

If the value in TCR\_ELx.T n SZ is outside the permitted range, then one of the following CONSTRAINED UNPREDICTABLE results occur:

- The TCR\_ELx.T n SZ value configures the bottom\_PAC\_bit value.
- The minimum permitted TCR\_ELx.T n SZ value configures the bottom\_PAC\_bit value.
- The maximum permitted TCR\_ELx.T n SZ value configures the bottom\_PAC\_bit value.

If a PE treats an out of range TCR\_ELx.T n SZ value as the maximum permitted field value or the minimum permitted field value for all purposes except reading the field value, then that behavior also applies to determining bottom\_PAC\_bit .

RVMZGK

RFCMCH

## D8.10.2 PAC generation and verification keys

IRSXKN

For pointer authentication, all of the following 128-bit PAC keys are provided:

- Instruction address PAC key A, APIAKey\_EL1, is the concatenation of the register values APIAKeyHi\_EL1:APIAKeyLo\_EL1.
- Instruction address PAC key B, APIBKey\_EL1, is the concatenation of the register values APIBKeyHi\_EL1:APIBKeyLo\_EL1.
- Data address PAC key A, APDAKey\_EL1, is the concatenation of the register values APDAKeyHi\_EL1:APDAKeyLo\_EL1.
- Data address PAC key B, APDBKey\_EL1, is the concatenation of the register values APDBKeyHi\_EL1:APDBKeyLo\_EL1.
- Generic authentication PAC key A, APGAKey\_EL1, is the concatenation of the register values APGAKeyHi\_EL1:APGAKeyLo\_EL1.

IKBYGG

For an Exception level, all of the following bits in the SCTLR\_ELx registers are used to enable PAC generation and validation:

- SCTLR\_ELx.EnIA enables instruction address pointer authentication using the APIAKey\_EL1 key.
- SCTLR\_ELx.EnIB enables instruction address pointer authentication using the APIBKey\_EL1 key.
- SCTLR\_ELx.EnDA enables data address pointer authentication using the APDAKey\_EL1 key.
- SCTLR\_ELx.EnDB enables data address pointer authentication using the APDBKey\_EL1 key.
- Software is expected to switch the PAC keys between Exception levels.
- Software is expected to not leave the values of the current keys present in memory, typically done by zeroing those locations after switching.

IGMQNP

All Exception levels use the same set of registers to hold PAC keys.

IGLRSR

When switching between Exception levels, software is expected to apply all of the following:

## D8.10.3 PAC instructions

| I VXGGK   | When a 64-bit general-purpose register is used as the target of an indirect branch instruction or the base register in a load instruction, all of the following instructions can be used to authenticate the register contents and prepare the register to be used: • Instructions that insert a PAC into the PAC field.                             |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I KCKSC   | An instruction that inserts a PAC into the PAC field of a 64-bit general-purpose register generates the PAC using the value of the 64-register and one or two other 64-bit diversifier values.                                                                                                                                                       |
| I WCZPC   | FEAT_PAuth_LR provides instructions that allow signing of the 64-bit value in LR against the value of SP and a PC-relative instruction address.                                                                                                                                                                                                      |
| R TMSKZ   | An instruction that inserts a PAC into the PAC field of a 64-bit general-purpose register, operates on the PAC field in one of the following ways:                                                                                                                                                                                                   |
| R TFBFT   | When FEAT_PAuth2 is not implemented and when performing a PAC operation on a non-canonical address then the PAC is modified to make it incorrect, and one of the following applies:                                                                                                                                                                  |
| I KBKGF   | - Otherwise, bit [54] is inverted. An instruction that extracts the PAC from the PAC field and checks that the value is correct does all of the following: • The check is based on the value of the register and one or two other 64-bit diversifier values.                                                                                         |
|           | • If the value is correct, the PAC is replaced with the extension bits. • If the value is incorrect, all of the following occur: - The PAC is replaced with the extension bits. - Two extension bits are set to a unique, fixed value, such that the 64-bit value represents a non-canonical VA. This is referred to as making the VA non-canonical. |
| I RZFZG   | Multiple versions of pointer authentication instructions support different use cases. Some instructions combine a pointer authentication operation with another operation.                                                                                                                                                                           |

| R WNKCJ   | If PAC generation and validation is disabled, then thePACGA and XPAC* instructions are not affected and are always enabled.                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R WDYDC   | If PAC generation and validation is disabled, then all of the following apply: • Instructions that insert a PAC into the address in a 64-bit general-purpose register execute as NOPs . • Instructions that authenticate a PAC execute as NOPs .                                                                                                                                                                                                                                                     |
| I RHMHV   | All of the following are examples of the resulting behavior of instructions that combine pointer authentication with another operation, if PAC generation and validation is disabled: • A RETAA instruction operates as a RET instruction.                                                                                                                                                                                                                                                           |
| I ZVGYK   | The PACGA instruction generates a 32-bit PAC from two 64-bit values and a generic key.                                                                                                                                                                                                                                                                                                                                                                                                               |
| I ZPGRZ   | The PACGA instruction can be used to protect small memory blocks. PACGA instructions can be chained to protect an arbitrary-sized memory block.                                                                                                                                                                                                                                                                                                                                                      |
| I PXWQC   | For pointer authentication instructions other than thePACGA instruction, the PAC is generated using one of the following IMPLEMENTATION DEFINED methods: • If FEAT_PACQARMA5 is implemented, then ID_AA64ISAR1_EL1.APA is nonzero and the QARMA5block cipher algorithm is used. • If FEAT_PACIMP is implemented, then ID_AA64ISAR1_EL1.API is nonzero and an IMPLEMENTATION DEFINED algorithm is used. • If FEAT_PACQARMA3 is implemented, then ID_AA64ISAR2_EL1.APA3 is nonzero and the QARMA3block |
| I WXMCQ   | For the PACGA instruction, the PAC is generated using one of the following IMPLEMENTATION DEFINED methods: • If FEAT_PACQARMA5 is implemented, then ID_AA64ISAR1_EL1.GPA is nonzero and the QARMA5block cipher algorithm is used. • If FEAT_PACIMP is implemented, then ID_AA64ISAR1_EL1.GPI is nonzero and an IMPLEMENTATION DEFINED algorithm is used. • If FEAT_PACQARMA3 is implemented, then ID_AA64ISAR2_EL1.GPA3 is nonzero and the QARMA3block                                               |
| R ZYPJV   | For a PAC generated using the ComputePAC() pseudocode function, where the PAC generation uses an IMPLEMENTATION DEFINED algorithm then the IMPLEMENTATION DEFINED algorithm uses the same arguments as the ComputePAC() function. For a PAC generated using the ComputePAC2() pseudocode function, where the PAC generation uses an IMPLEMENTATION DEFINED algorithm then the IMPLEMENTATION DEFINED algorithm uses the same arguments as the ComputePAC2() function.                                |
| R JTRCS   | For a set of arguments passed to the ComputePAC() or ComputePAC2() pseudocode function, the same result is produced by all PEs that an execution thread could migrate between.                                                                                                                                                                                                                                                                                                                       |
| R DPXKM   | The ComputePAC2() pseudocode function generates a PAC for 64-bit data, using a 128-bit PAC key and two diversifiers.                                                                                                                                                                                                                                                                                                                                                                                 |
| R MLLDB   | If ComputePAC2() is implemented using FEAT_PACQARMA5 or FEAT_PACQARMA3, then the two diversifiers are concatenated into a single 64-bit diversifier as follows: • Bits[31:0] of the 64-bit diversifier hold the value modifier1<35:4>. • Bits[63:32] of the 64-bit diversifier hold the value modifier2<36:5>.                                                                                                                                                                                       |
| I RNXPW   | Arm strongly recommends that software at EL0 does not mix pointer authentication mechanisms. For example, using the PACGA instruction to create a PAC and using other pointer authentication instructions to authenticate, or using an instruction which uses a specific key to sign a pointer and using an instruction which uses a different key to authenticate that pointer.                                                                                                                     |

## D8.10.4 PSTATE.PACM

| R BYRKF   | All statements in this section require implementation of FEAT_PAuth_LR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TQTGT   | PSTATE and the PACMinstruction provide a mechanism to produce a program that can run on a PE that implements FEAT_PAuth_LR or on a PE that does not implement FEAT_PAuth_LR, by extending the behavior of existing instructions for signing and authenticating a return address.                                                                                                                                                                                                                                                                                                                                                                                    |
| I RZKKL   | PACM is intended to be executed immediately before a PACIASP , PACIBSP , AUTIASP , AUTIBSP , RETAA , RETAB , AUTIA1716 , AUTIB1716 , PACIA1716 , or PACIB1716 instruction, to extend the operation of those instructions to take a second diversifier.                                                                                                                                                                                                                                                                                                                                                                                                              |
| R PLWLR   | Unless otherwise specified, PSTATE.PACM is set to 0 after execution of any instruction..                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R GJJYJ   | If an IMPLEMENTATION DEFINED algorithm is implemented for Pointer authentication instructions other than the PACGA instruction, PSTATE.PACM is permitted to be a trivial implementation. Otherwise, PSTATE.PACM is fully implemented.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| I LYDML   | For a trivial implementation of PSTATE.PACM, all of the following apply: • The PACM instruction does not set PSTATE.PACM to 1. • The effects of PACM instructions are disabled at all Exception levels and PSTATE.PACM behaves as 0. • SPSR_ELx.PACM, DSPSR_EL0.PACM, HCRX_EL2.PACMEn, and SCTLR2_ELx.{EnPACM0, EnPACM} are fully implemented, although a value of 1 in these fields has no effect other than for reading back the value of the register.                                                                                                                                                                                                           |
|           | Note If FEAT_PACIMP is implemented, then use of PSTATE.PACM to modify the behavior of a subsequent instruction might not result in the same PAC field insertion or authentication as the explicit instructions. For example, use of PSTATE.PACM to modify a subsequent PACIASP instruction might not result in the same PAC field insertion as a PACIASPPC instruction at the same PC as the PACIASP . This means that software should not mix the methods used to sign and authenticate a pointer, and should use a single method for a specific pointer.                                                                                                          |
| R TQKBS   | For a full implementation of PSTATE.PACM, if the effects of PACM instructions are enabled, then PSTATE.PACM is set to 1 after execution of a PACM instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R WNZMT   | If PSTATE.PACM is 1, then the behavior of the PACIASP , PACIBSP , AUTIASP , AUTIBSP , RETAA , RETAB , AUTIA1716 , AUTIB1716 , PACIA1716 , and PACIB1716 instructions are extended as follows: • The pseudocode function ComputePAC2() is used for the generation of the PAC. SeeR ZYPJV . • For the PACIASP and PACIBSP instructions, the 64-bit value of modifier2 used in the generation of the PAC is the value specified in the PC. • For the AUTIASP , AUTIBSP , RETAA , and RETAB instructions, the 64-bit value of modifier2 is the value in X16. • For the AUTIA1716 , AUTIB1716 , PACIA1716 , and PACIB1716 instructions, the 64-bit value of modifier2 is |
| I SRKXB   | Each of the SCTLR2_ELx.{EnPACM, EnPACM0} control bits enables or disables the effect of the PACM instruction at an Exception level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I HBWFK   | The HCRX_EL2.PACMEn bit can control the effect of a PACM instruction at EL1 and EL0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I RVHSQ   | If the effects of PACM instructions are disabled at an Exception level, PSTATE.PACM cannot be set to 1 at that Exception level and is consistent with being treated as 0 at that Exception level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| I CDWGZ   | When the PACM instruction is used, to ensure code is fully backward compatible with a PE that does not implement FEAT_PAuth_LR, a BTI instruction must be used in the function prologue. For more information, see PSTATE.BTYPE.                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## D8.10.5 Faulting on pointer authentication

IXBGSY APACauthentication failure for a given VA can cause a fault to be generated in the following three manners, according to the type of the instruction and whether FEAT\_FPAC and FEAT\_FPACCOMBINE are implemented:

- The PAC instruction makes the VA non-canonical, such that a subsequent use of the V A generates a fault. In this case, the PAC instruction does not directly generate the fault.
- The PAC instruction makes the VA non-canonical and uses that V A such that a fault is generated by that instruction.
- The PAC instruction directly generates a PAC Fail exception, with EC code 0b011100 .

RMLWGL If an instruction is a combined instruction that includes pointer authentication, then when the PAC is incorrect in a given VA, one of the following behaviors occurs:

- For a combined authenticate and load instruction, then:
- -If FEAT\_FPACCOMBINE is not implemented, the VA is made non-canonical and then used as the address for the load.
- -If FEAT\_FPACCOMBINE is implemented, then the instruction generates a PAC Fail exception, with EC code 0b011100 .
- For a combined authenticate and branch instruction, then:
- -If FEAT\_FPACCOMBINE is not implemented, the VA is made non-canonical and the PC is updated to this non-canonical value.
- -If FEAT\_FPACCOMBINE is implemented, then the instruction generates a PAC Fail exception, with EC code 0b011100 .

RKJSRQ For a PAC authentication instruction, AUT* , when the PAC is incorrect for a given V A, one of the following behaviors occurs:

- If FEAT\_FPAC is not implemented, the VA is made non-canonical.
- If FEAT\_FPAC is implemented, then the instruction generates a PAC Fail exception, with EC code 0b011100 .

Predicting the result of a PAC Authentication is a form of control flow prediction.

Prediction of the results of a PAC Authentication must adhere to the requirements of FEAT\_FPACC\_SPEC, if implemented.

RXXFXH

- RGKVYD