## D20.7 Error records in the PE

IKMMPK Acomponent that records detected errors is called a node by the RAS System Architecture. Each node implements one or more Error records.

RVNLPC It is IMPLEMENTATION DEFINED whether the processor that implements a PE implements any nodes.

RXKDRX APEimplementing the RAS Extension might implement the System register interface to nodes.

ISCVSB

The System register interface to nodes is not restricted to accessing only PE nodes.

IZRKKQ

When an error is recorded by a PE node, one or more of the following might be generated, according to the configuration of the node:

- AFault handling interrupt.
- An Error recovery interrupt.
- ACritical Error interrupt.
- An in-band error response.

## D20.7.1 Error record System register view

| I SLVDW   | If the System register interface to a node is implemented, then software can access the Error records of the node using Error record System registers.                                                                                                                                                                                                                                                                                                                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BYLZQ   | The number of Error records that can be accessed using the System registers is IMPLEMENTATION DEFINED, and might be zero. The ERRIDR_EL1 and ERRIDR registers indicate the highest numbered index of the Error records that can be accessed using System registers, plus one.                                                                                                                                                                                          |
| I NWBNQ   | The AArch64 Error record System registers are those registers with an ERX*_EL1 mnemonic. The AArch32 Error record System registers are those registers with an ERX* mnemonic.                                                                                                                                                                                                                                                                                          |
| I BJNDF   | The following tables describe the AArch32 and AArch64 Error record System registers. The descriptions in this section apply whether the Error record is accessed through the indirection mechanism, as described in Table D20-2 and Table D20-3, or as memory-mapped registers. For more information on the RAS memory-mapped registers, see Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100). |

Table D20-2 Using AArch32 System registers, System register map

| Use        | To Access          | Access   | Description                                 |
|------------|--------------------|----------|---------------------------------------------|
| ERXADDR    | ERR<n>ADDR[31:0]   | RW       | Error Record < n > Address Register         |
| ERXADDR2   | ERR<n>ADDR[63:32]  | RW       | Error Record < n > Address Register         |
| ERXCTLR    | ERR<n>CTLR[31:0]   | RW       | Error Record < n > Control Register         |
| ERXCTLR2   | ERR<n>CTLR[63:32]  | RW       | Error Record < n > Control Register         |
| ERXFR      | ERR<n>FR[31:0]     | RO       | Error Record < n > Feature Register         |
| ERXFR2     | ERR<n>FR[63:32]    | RO       | Error Record < n > Feature Register         |
| ERXMISC0   | ERR<n>MISC0[31:0]  | RW       | Error Record < n > Miscellaneous Register 0 |
| ERXMISC1   | ERR<n>MISC0[63:32] | RW       | Error Record < n > Miscellaneous Register 0 |
| ERXMISC2   | ERR<n>MISC1[31:0]  | RW       | Error Record < n > Miscellaneous Register 1 |
| ERXMISC3   | ERR<n>MISC1[63:32] | RW       | Error Record < n > Miscellaneous Register 1 |
| ERXMISC4 a | ERR<n>MISC2[31:0]  | RW       | Error Record < n > Miscellaneous Register 2 |

| Use        | To Access          | Access   | Description                                 |
|------------|--------------------|----------|---------------------------------------------|
| ERXMISC5 a | ERR<n>MISC2[63:32] | RW       | Error Record < n > Miscellaneous Register 2 |
| ERXMISC6 a | ERR<n>MISC3[31:0]  | RW       | Error Record < n > Miscellaneous Register 3 |
| ERXMISC7 a | ERR<n>MISC3[63:32] | RW       | Error Record < n > Miscellaneous Register 3 |
| ERXSTATUS  | ERR<n>STATUS       | RW       | Error Record < n > Primary Status Register  |

a. If FEAT\_RASv1p1 is implemented.

RZBCFZ

RMBSFP

SVBBNY

IWKXSB

IJMVVD

RWFPWF

RFZBLM

## Table D20-3 Using AArch64 System registers, System register map

| Use            | To Access    | Access   | Description                                                   |
|----------------|--------------|----------|---------------------------------------------------------------|
| ERXADDR_EL1    | ERR<n>ADDR   | RW       | Error Record < n > Address Register                           |
| ERXCTLR_EL1    | ERR<n>CTLR   | RW       | Error Record < n > Control Register                           |
| ERXFR_EL1      | ERR<n>FR     | RO       | Error Record < n > Feature Register                           |
| ERXMISC0_EL1   | ERR<n>MISC0  | RW       | Error Record < n > Miscellaneous Register 0                   |
| ERXMISC1_EL1   | ERR<n>MISC1  | RW       | Error Record < n > Miscellaneous Register 1                   |
| ERXMISC2_EL1 a | ERR<n>MISC2  | RW       | Error Record < n > Miscellaneous Register 2                   |
| ERXMISC3_EL1 a | ERR<n>MISC3  | RW       | Error Record < n > Miscellaneous Register 3                   |
| ERXPFGCDN_EL1  | ERR<n>PFGCDN | RW       | Error Record < n > Pseudo-fault Generation Countdown Register |
| ERXPFGCTL_EL1  | ERR<n>PFGCTL | RW       | Error Record < n > Pseudo-fault Generation Control Register   |
| ERXPFGF_EL1    | ERR<n>PFGF   | RO       | Error Record < n > Pseudo-fault Generation Feature Register   |
| ERXSTATUS_EL1  | ERR<n>STATUS | RW       | Error Record < n > Primary Status Register                    |
| ERXGSR_EL1 b   | ERRGSR{<n>}  | RO       | Error Group Status Register                                   |

a. If FEAT\_RASv1p1 is implemented.

b. If FEAT\_RASv2 is implemented.

If FEAT\_RASv1p1 is implemented, then all Error records accessible through System registers implement RAS System

Architecture version 1.1.

If FEAT\_RASv2 is implemented, then all Error records accessible through System registers implement RAS System

Architecture version 2.

To access an Error record, software:

1. Sets the error selection register, ERRSELR\_EL1.SEL or ERRSELR.SEL, to the index of the record being accessed.
2. Accesses the Error record using the ERX*\_EL1 or ERX* System registers, as described in IBJNDF.

The Error records accessed through the System registers might be accessible only to the PE associated with those System registers, or they might be shared and therefore accessible to other PEs through either System registers or as a

memory-mapped component.

Direct reads of the System registers, including Error record System registers, can occur speculatively and out-of-order relative to other instructions executed on the same PE.

Direct reads and writes of the Error records through the ERX*\_EL1 AArch64 System registers, as described in IBJNDF, are indirect reads of ERRSELR\_EL1.

Direct reads and writes of the Error records through the ERX* AArch32 System registers, as described in IBJNDF, are indirect reads of ERRSELR.

IYMGGY

IRGMHN

RSLNMV

Explicit synchronization is required after reading an ERXGSR\_EL1 AArch64 System register and before reading ERXSTATUS\_EL1.

## Example D20-16 Direct reads of ERXGSR\_EL1 cause indirect reads of ERRSELR\_EL1

1. An instruction A writes the value &lt;n&gt; to ERRSELR\_EL1.SEL. &lt;n&gt; is the index of an implemented System register error record.
2. Software executes a first Context synchronization event B in program order after A.
3. An instruction C in program order after B reads ERXGSR\_EL1, and observes bit [n MOD 64] == 0b1 .
4. Software executes a second Context synchronization event D in program order after C.
5. An instruction E in program order after D reads ERXSTATUS\_EL1.

If there is no other direct or external write to ERR&lt;n&gt;STATUS that clears ERR&lt;n&gt;STATUS.V between C and E, then instruction E observes ERR&lt;n&gt;STATUS.V == 0b1 .

## D20.7.1.1 Syndrome registers

ESR\_ELx, HSR, and DFSR are exception syndrome registers. The PE records syndrome information in an exception syndrome register on taking a physical SError exception or synchronous External abort exception. ESR\_ELx, HSR, and DFSR are also used by other exceptions.

DISR\_EL1 and DISR are the deferred error syndrome registers. The PE records syndrome information in a deferred error syndrome register on deferring a physical SError exception.

The PE also records a virtual syndrome value in ESR\_EL1, DFSR, DISR\_EL1, or DISR on taking or deferring a virtual SError exception. The virtual syndrome value is provided by software in a corresponding virtual error syndrome register, VSESR\_EL2, VDFSR, VDISR\_EL2, or VDISR respectively.

The PE also records a delegated syndrome value in ESR\_EL2, ESR\_EL1, VDISR\_EL2, or DISR\_EL1 on taking or deferring a delegated SError exception. The delegated syndrome value is provided by software in a corresponding delegated error syndrome register, VSESR\_EL3 or VDISR\_EL3 respectively.

For a given implementation:

- If ESB never synchronizes any errors, then DISR\_EL1.A and DISR.A might be RES0.
- The deferred, virtual, and delegated syndrome registers are capable of storing any syndrome value that might be recorded by the PE in an exception syndrome register on taking a physical SError exception or synchronous External abort exception.
- If any of ESR\_ELx[24:0], HSR[11:9], and DFSR[15:14,12] is not used and always set to zero by the PE on taking a physical SError exception or synchronous External abort exception, then that bit can be RES0 in that exception syndrome register.
- Abit that is not used and always set to zero or always set to one in ESR\_ELx or DISR\_EL1 by the PE on taking a physical SError exception is permitted to be RES0 or RES1 respectively in the corresponding deferred, virtual, and delegated error syndrome registers. See Table D20-4.

In Table D20-4, the deferred virtual, or delegated error syndrome register bit described in the left-hand column is permitted to be RES0 or RES1 only if the corresponding bit is always set to zero or always set to one (respectively) on taking a physical SError exception in all of the implemented exception syndrome registers listed in the other columns marked Yes on that row. Otherwise, the bit is read/write.

Table D20-4 Permitted relaxations for bits in deferred, virtual, and delegated error syndrome registers

| Bit is permitted to be res0 or res1   | ESR_ELx[ n ] n ∈ [24:0]   | HSR[ n ] n ∈ [11:9]   | DFSR[ n ] n ∈ [15:14,12]   |
|---------------------------------------|---------------------------|-----------------------|----------------------------|
| VSESR_EL3[ n ]                        | Yes                       | -                     | -                          |
| VDISR_EL3[ n ]                        | Yes                       | -                     | -                          |
| VSESR_EL2[ n ]                        | Yes                       | -                     | Yes                        |
| VDISR_EL2[ n ]                        | Yes                       | -                     | Yes                        |
| DISR_EL1[ n ]                         | Yes                       | -                     | -                          |

| Bit is permitted to be res0 or res1   | ESR_ELx[ n ] n ∈ [24:0]   | HSR[ n ] n ∈ [11:9]   | DFSR[ n ] n ∈ [15:14,12]   |
|---------------------------------------|---------------------------|-----------------------|----------------------------|
| VDFSR[ n ]                            | -                         | -                     | Yes                        |
| VDISR[ n ]                            | -                         | -                     | Yes                        |
| DISR[ n ]                             | -                         | Yes                   | Yes                        |

IFWGLF

RSLNMV means that VSESR\_EL3, VSESR\_EL2 and VDFSR can be implemented as RAZ/WI when ESR\_ELx[24:0], HSR[11:9], and DFSR[15:14,12] are always set to zero by the PE on taking a physical SError exception or synchronous External abort exception. When this is the case, the PE error state is always reported as Uncategorized error when a physical SError exception is taken to AArch64 state.

IGQQCK, in Error synchronization barriers in a minimal implementation then further allows ESB to be executed as a NOP, meaning DISR\_EL1, DISR, VDISR\_EL2, VDISR\_EL3, and VDISR can also be implemented as RAZ/WI.

This allows for a very low-cost implementation of the RAS Extension.

## Chapter D21 MPAM PE Architecture

This chapter describes the MPAM Extension PE Architecture. It contains the following sections:

- About MPAM.
- PARTID spaces.
- Partition Identifiers (PARTIDs).
- Performance Monitoring Groups (PMGs).
- Effect of the MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls on PE Secure state execution.
- Effect of access type on MPAM information.
- Virtualization support.
- MPAMPE-side Maximum-bandwidth limit injection control.
- MPAMerrors.
- Synchronization of MPAM System register changes.