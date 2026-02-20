## D23.2 Moves to and from debug and trace System registers

The instructions that move data to and from the debug, execution environment, and trace System registers are encoded with op0 == 0b10 . This means the encoding of these instructions is:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18   | 16 15   | 12 11   | 8 7   |
|---------------------------------------------|---------|---------|-------|
| 1 1 0 1 0 1 0 1 0 0 L op1 1 0               | CRn     | CRm     |       |

op0

Note

- The section describes the use of all of the op0 == 0b10 region of the System register encoding space.
- These encodings access the registers that are equivalent to the AArch32 System registers in the ( coproc == 0b1110 ) encoding space.

The value of op1 provides the next level of decode of these instructions, as follows:

op1 == { 0b000 , 0b011 , 0b100 , 0b101 , 0b110 , 0b111 }

Debug, PMU, and System PMU registers.

Note

The standard encoding of debug registers is op0 == 0b10 , op1 == {0, 3, 4}. The registers in the op0 == 0b11 encoding space that are classified as debug registers are DLR\_EL0, DSPSR\_EL0, MDCR\_EL2, MDCR\_EL3, and SDER32\_EL3. See Instructions for accessing non-debug System registers for the encodings of these registers.

op1 == { 0b001 } Trace and BRBE registers.

## D23.2.1 Instructions for accessing debug System registers

The instructions for accessing debug System registers are:

| MSR <System_register>, Xt   | ; Write to System register   |
|-----------------------------|------------------------------|
| MRS Xt, <System_register>   | ; Read from System register  |

Where &lt;System\_register&gt; is the register name, for example MDCCSR\_EL0.

This section includes only the System register access encodings for which both:

- op0 is 0b10 .
- The value of op1 is one of { 0b000 , 0b001 , 0b011 , 0b100 , 0b101 , 0b110 , 0b111 }.

Note

These encodings access the registers that are equivalent to the AArch32 System registers in the ( coproc == 0b1110 ) encoding space. For more information, see Mapping of the System registers between the Execution states.

Table D23-1 shows the mapping of the System register encodings for debug System register access.

Table D23-1 Instruction encodings for debug System register access in the (op0==0b10) encoding space

| op1   | CRn    | CRm    | op2        | Access   | Mnemonic          | Accesses                      |
|-------|--------|--------|------------|----------|-------------------|-------------------------------|
| 0b000 | 0b0000 | 0b0000 | 0b010      | RW       | OSDTRRX_EL1       | OSDTRRX_EL1                   |
| 0b000 | 0b0000 | 0b0010 | 0b000      | RW       | MDCCINT_EL1       | MDCCINT_EL1                   |
| 0b000 | 0b0000 | 0b0010 | 0b010      | RW       | MDSCR_EL1         | MDSCR_EL1                     |
| 0b000 | 0b0000 | 0b0011 | 0b010      | RW       | OSDTRTX_EL1       | OSDTRTX_EL1                   |
| 0b000 | 0b0000 | 0b0100 | 0b010      | RW       | MDSELR_EL1        | MDSELR_EL1                    |
| 0b000 | 0b0000 | 0b0101 | 0b010      | RW       | MDSTEPOP_EL1      | MDSTEPOP_EL1                  |
| 0b000 | 0b0000 | 0b0110 | 0b010      | RW       | OSECCR_EL1        | OSECCR_EL1                    |
| 0b000 | 0b0000 | m[3:0] | 0b100      | RW       | DBGBVR<m>_EL1     | DBGBVR<n>_EL1                 |
| 0b000 | 0b0000 | m[3:0] | 0b101      | RW       | DBGBCR<m>_EL1     | DBGBCR<n>_EL1                 |
| 0b000 | 0b0000 | m[3:0] | 0b110      | RW       | DBGWVR<m>_EL1     | DBGWVR<n>_EL1                 |
| 0b000 | 0b0000 | m[3:0] | 0b111      | RW       | DBGWCR<m>_EL1     | DBGWCR<n>_EL1                 |
| 0b000 | 0b0001 | 0b0000 | 0b000      | RO       | MDRAR_EL1         | MDRAR_EL1                     |
| 0b000 | 0b0001 | 0b0000 | 0b100      | WO       | OSLAR_EL1         | OSLAR_EL1                     |
| 0b000 | 0b0001 | 0b0001 | 0b100      | RO       | OSLSR_EL1         | OSLSR_EL1                     |
| 0b000 | 0b0001 | 0b0011 | 0b100      | RW       | OSDLR_EL1         | OSDLR_EL1                     |
| 0b000 | 0b0001 | 0b0100 | 0b100      | RW       | DBGPRCR_EL1       | DBGPRCR_EL1                   |
| 0b000 | 0b0111 | 0b1000 | 0b110      | RW       | DBGCLAIMSET_EL1   | DBGCLAIMSET_EL1               |
| 0b000 | 0b0111 | 0b1001 | 0b110      | RW       | DBGCLAIMCLR_EL1   | DBGCLAIMCLR_EL1               |
| 0b000 | 0b0111 | 0b1110 | 0b110      | RO       | DBGAUTHSTATUS_EL1 | DBGAUTHSTATUS_EL1             |
| 0b000 | 0b1001 | 0b1101 | 0b00 :m[0] | RO       | SPMCGCR<m>_EL1    | SPMCGCR<n>_EL1                |
| 0b000 | 0b1001 | 0b1101 | 0b011      | RW       | SPMACCESSR_EL1    | SPMACCESSR_EL1 SPMACCESSR_EL2 |
| 0b000 | 0b1001 | 0b1101 | 0b100      | RO       | SPMIIDR_EL1       | SPMIIDR_EL1                   |

| op1   | CRn    | CRm          | op2    | Access   | Mnemonic          | Accesses          |
|-------|--------|--------------|--------|----------|-------------------|-------------------|
| 0b000 | 0b1001 | 0b1101       | 0b101  | RO       | SPMDEVARCH_EL1    | SPMDEVARCH_EL1    |
| 0b000 | 0b1001 | 0b1101       | 0b110  | RO       | SPMDEVAFF_EL1     | SPMDEVAFF_EL1     |
| 0b000 | 0b1001 | 0b1101       | 0b111  | RO       | SPMCFGR_EL1       | SPMCFGR_EL1       |
| 0b000 | 0b1001 | 0b1110       | 0b001  | RW       | SPMINTENSET_EL1   | SPMINTENSET_EL1   |
| 0b000 | 0b1001 | 0b1110       | 0b010  | RW       | SPMINTENCLR_EL1   | SPMINTENCLR_EL1   |
| 0b000 | 0b1110 | 0b1011       | 0b111  | RO       | PMCCNTSVR_EL1     | PMCCNTSVR_EL1     |
| 0b000 | 0b1110 | 0b10 :m[4:3] | m[2:0] | RO       | PMEVCNTSVR<m>_EL1 | PMEVCNTSVR<n>_EL1 |
| 0b000 | 0b1110 | 0b1100       | 0b000  | RO       | PMICNTSVR_EL1     | PMICNTSVR_EL1     |
| 0b001 | 0b0000 | 0b0000       | 0b001  | RW       | TRCTRACEIDR       | TRCTRACEIDR       |
| 0b001 | 0b0000 | 0b0000       | 0b010  | RW       | TRCVICTLR         | TRCVICTLR         |
| 0b001 | 0b0000 | 0b0000       | 0b110  | RO       | TRCIDR8           | TRCIDR8           |
| 0b001 | 0b0000 | 0b0000       | 0b111  | RW       | TRCIMSPEC0        | TRCIMSPEC0        |
| 0b001 | 0b0000 | 0b0001       | 0b000  | RW       | TRCPRGCTLR        | TRCPRGCTLR        |
| 0b001 | 0b0000 | 0b0001       | 0b001  | RW       | TRCQCTLR          | TRCQCTLR          |
| 0b001 | 0b0000 | 0b0001       | 0b010  | RW       | TRCVIIECTLR       | TRCVIIECTLR       |
| 0b001 | 0b0000 | 0b0001       | 0b110  | RO       | TRCIDR9           | TRCIDR9           |
| 0b001 | 0b0000 | 0b0010       | 0b001  | RW       | TRCITEEDCR        | TRCITEEDCR        |
| 0b001 | 0b0000 | 0b0010       | 0b010  | RW       | TRCVISSCTLR       | TRCVISSCTLR       |
| 0b001 | 0b0000 | 0b0010       | 0b110  | RO       | TRCIDR10          | TRCIDR10          |
| 0b001 | 0b0000 | 0b0011       | 0b000  | RO       | TRCSTATR          | TRCSTATR          |
| 0b001 | 0b0000 | 0b0011       | 0b010  | RW       | TRCVIPCSSCTLR     | TRCVIPCSSCTLR     |
| 0b001 | 0b0000 | 0b0011       | 0b110  | RO       | TRCIDR11          | TRCIDR11          |
| 0b001 | 0b0000 | 0b00 :m[1:0] | 0b100  | RW       | TRCSEQEVR<m>      | TRCSEQEVR<n>      |
| 0b001 | 0b0000 | 0b00 :m[1:0] | 0b101  | RW       | TRCCNTRLDVR<m>    | TRCCNTRLDVR<n>    |
| 0b001 | 0b0000 | 0b0100       | 0b000  | RW       | TRCCONFIGR        | TRCCONFIGR        |
| 0b001 | 0b0000 | 0b0100       | 0b110  | RO       | TRCIDR12          | TRCIDR12          |
| 0b001 | 0b0000 | 0b0101       | 0b110  | RO       | TRCIDR13          | TRCIDR13          |
| 0b001 | 0b0000 | 0b0110       | 0b000  | RW       | TRCAUXCTLR        | TRCAUXCTLR        |
| 0b001 | 0b0000 | 0b0110       | 0b100  | RW       | TRCSEQRSTEVR      | TRCSEQRSTEVR      |
| 0b001 | 0b0000 | 0b0111       | 0b100  | RW       | TRCSEQSTR         | TRCSEQSTR         |
| 0b001 | 0b0000 | 0b01 :m[1:0] | 0b101  | RW       | TRCCNTCTLR<m>     | TRCCNTCTLR<n>     |
| 0b001 | 0b0000 | 0b0 :m[2:0]  | 0b111  | RW       | TRCIMSPEC<m>      | TRCIMSPEC<n>      |
| 0b001 | 0b0000 | 0b1000       | 0b000  | RW       | TRCEVENTCTL0R     | TRCEVENTCTL0R     |
| 0b001 | 0b0000 | 0b1000       | 0b111  | RO       | TRCIDR0           | TRCIDR0           |
| 0b001 | 0b0000 | 0b1001       | 0b000  | RW       | TRCEVENTCTL1R     | TRCEVENTCTL1R     |
| 0b001 | 0b0000 | 0b1001       | 0b111  | RO       | TRCIDR1           | TRCIDR1           |
| 0b001 | 0b0000 | 0b1010       | 0b000  | RW       | TRCRSR            | TRCRSR            |
| 0b001 | 0b0000 | 0b1010       | 0b111  | RO       | TRCIDR2           | TRCIDR2           |
| 0b001 | 0b0000 | 0b1011       | 0b000  | RW       | TRCSTALLCTLR      | TRCSTALLCTLR      |
| 0b001 | 0b0000 | 0b1011       | 0b111  | RO       | TRCIDR3           | TRCIDR3           |

| op1   | CRn    | CRm          | op2        | Access   | Mnemonic        | Accesses            |
|-------|--------|--------------|------------|----------|-----------------|---------------------|
| 0b001 | 0b0000 | 0b10 :m[1:0] | 0b100      | RW       | TRCEXTINSELR<m> | TRCEXTINSELR<n>     |
| 0b001 | 0b0000 | 0b10 :m[1:0] | 0b101      | RW       | TRCCNTVR<m>     | TRCCNTVR<n>         |
| 0b001 | 0b0000 | 0b1100       | 0b000      | RW       | TRCTSCTLR       | TRCTSCTLR           |
| 0b001 | 0b0000 | 0b1100       | 0b111      | RO       | TRCIDR4         | TRCIDR4             |
| 0b001 | 0b0000 | 0b1101       | 0b000      | RW       | TRCSYNCPR       | TRCSYNCPR           |
| 0b001 | 0b0000 | 0b1101       | 0b111      | RO       | TRCIDR5         | TRCIDR5             |
| 0b001 | 0b0000 | 0b1110       | 0b000      | RW       | TRCCCCTLR       | TRCCCCTLR           |
| 0b001 | 0b0000 | 0b1110       | 0b111      | RO       | TRCIDR6         | TRCIDR6             |
| 0b001 | 0b0000 | 0b1111       | 0b000      | RW       | TRCBBCTLR       | TRCBBCTLR           |
| 0b001 | 0b0000 | 0b1111       | 0b111      | RO       | TRCIDR7         | TRCIDR7             |
| 0b001 | 0b0001 | 0b0001       | 0b100      | RO       | TRCOSLSR        | TRCOSLSR            |
| 0b001 | 0b0001 | 0b0 :m[2:0]  | 0b010      | RW       | TRCSSCCR<m>     | TRCSSCCR<n>         |
| 0b001 | 0b0001 | 0b0 :m[2:0]  | 0b011      | RW       | TRCSSPCICR<m>   | TRCSSPCICR<n>       |
| 0b001 | 0b0001 | 0b1 :m[2:0]  | 0b010      | RW       | TRCSSCSR<m>     | TRCSSCSR<n>         |
| 0b001 | 0b0001 | m[3:0]       | 0b00 :m[4] | RW       | TRCRSCTLR<m>    | TRCRSCTLR<n>        |
| 0b001 | 0b0010 | m[2:0]: 0b0  | 0b00 :m[3] | RW       | TRCACVR<m>      | TRCACVR<n>          |
| 0b001 | 0b0010 | m[2:0]: 0b0  | 0b01 :m[3] | RW       | TRCACATR<m>     | TRCACATR<n>         |
| 0b001 | 0b0011 | 0b0000       | 0b010      | RW       | TRCCIDCCTLR0    | TRCCIDCCTLR0        |
| 0b001 | 0b0011 | 0b0001       | 0b010      | RW       | TRCCIDCCTLR1    | TRCCIDCCTLR1        |
| 0b001 | 0b0011 | 0b0010       | 0b010      | RW       | TRCVMIDCCTLR0   | TRCVMIDCCTLR0       |
| 0b001 | 0b0011 | 0b0011       | 0b010      | RW       | TRCVMIDCCTLR1   | TRCVMIDCCTLR1       |
| 0b001 | 0b0011 | m[2:0]: 0b0  | 0b000      | RW       | TRCCIDCVR<m>    | TRCCIDCVR<n>        |
| 0b001 | 0b0011 | m[2:0]: 0b0  | 0b001      | RW       | TRCVMIDCVR<m>   | TRCVMIDCVR<n>       |
| 0b001 | 0b0111 | 0b0010       | 0b111      | RO       | TRCDEVID        | TRCDEVID            |
| 0b001 | 0b0111 | 0b1000       | 0b110      | RW       | TRCCLAIMSET     | TRCCLAIMSET         |
| 0b001 | 0b0111 | 0b1001       | 0b110      | RW       | TRCCLAIMCLR     | TRCCLAIMCLR         |
| 0b001 | 0b0111 | 0b1110       | 0b110      | RO       | TRCAUTHSTATUS   | TRCAUTHSTATUS       |
| 0b001 | 0b0111 | 0b1111       | 0b110      | RO       | TRCDEVARCH      | TRCDEVARCH          |
| 0b001 | 0b1000 | m[3:0]       | m[4]: 0b00 | RO       | BRBINF<m>_EL1   | BRBINF<n>_EL1       |
| 0b001 | 0b1000 | m[3:0]       | m[4]: 0b01 | RO       | BRBSRC<m>_EL1   | BRBSRC<n>_EL1       |
| 0b001 | 0b1000 | m[3:0]       | m[4]: 0b10 | RO       | BRBTGT<m>_EL1   | BRBTGT<n>_EL1       |
| 0b001 | 0b1001 | 0b0000       | 0b000      | RW       | BRBCR_EL1       | BRBCR_EL1 BRBCR_EL2 |
| 0b001 | 0b1001 | 0b0000       | 0b001      | RW       | BRBFCR_EL1      | BRBFCR_EL1          |
| 0b001 | 0b1001 | 0b0000       | 0b010      | RW       | BRBTS_EL1       | BRBTS_EL1           |
| 0b001 | 0b1001 | 0b0001       | 0b000      | RW       | BRBINFINJ_EL1   | BRBINFINJ_EL1       |
| 0b001 | 0b1001 | 0b0001       | 0b001      | RW       | BRBSRCINJ_EL1   | BRBSRCINJ_EL1       |
| 0b001 | 0b1001 | 0b0001       | 0b010      | RW       | BRBTGTINJ_EL1   | BRBTGTINJ_EL1       |
| 0b001 | 0b1001 | 0b0010       | 0b000      | RO       | BRBIDR0_EL1     | BRBIDR0_EL1         |
| 0b011 | 0b0000 | 0b0001       | 0b000      | RO       | MDCCSR_EL0      | MDCCSR_EL0          |

| op1   | CRn    | CRm         | op2    | Access   | Mnemonic           | Accesses           |
|-------|--------|-------------|--------|----------|--------------------|--------------------|
| 0b011 | 0b0000 | 0b0100      | 0b000  | RW       | DBGDTR_EL0         | DBGDTR_EL0         |
| 0b011 | 0b0000 | 0b0101      | 0b000  | RO       | DBGDTRRX_EL0       | DBGDTRRX_EL0       |
| 0b011 | 0b0000 | 0b0101      | 0b000  | WO       | DBGDTRTX_EL0       | DBGDTRTX_EL0       |
| 0b011 | 0b1001 | 0b1100      | 0b000  | RW       | SPMCR_EL0          | SPMCR_EL0          |
| 0b011 | 0b1001 | 0b1100      | 0b001  | RW       | SPMCNTENSET_EL0    | SPMCNTENSET_EL0    |
| 0b011 | 0b1001 | 0b1100      | 0b010  | RW       | SPMCNTENCLR_EL0    | SPMCNTENCLR_EL0    |
| 0b011 | 0b1001 | 0b1100      | 0b011  | RW       | SPMOVSCLR_EL0      | SPMOVSCLR_EL0      |
| 0b011 | 0b1001 | 0b1100      | 0b100  | WO       | SPMZR_EL0          | SPMZR_EL0          |
| 0b011 | 0b1001 | 0b1100      | 0b101  | RW       | SPMSELR_EL0        | SPMSELR_EL0        |
| 0b011 | 0b1001 | 0b1110      | 0b011  | RW       | SPMOVSSET_EL0      | SPMOVSSET_EL0      |
| 0b011 | 0b1110 | 0b000 :m[3] | m[2:0] | RW       | SPMEVCNTR<m>_EL0   | SPMEVCNTR<n>_EL0   |
| 0b011 | 0b1110 | 0b001 :m[3] | m[2:0] | RW       | SPMEVTYPER<m>_EL0  | SPMEVTYPER<n>_EL0  |
| 0b011 | 0b1110 | 0b010 :m[3] | m[2:0] | RW       | SPMEVFILTR<m>_EL0  | SPMEVFILTR<n>_EL0  |
| 0b011 | 0b1110 | 0b011 :m[3] | m[2:0] | RW       | SPMEVFILT2R<m>_EL0 | SPMEVFILT2R<n>_EL0 |
| 0b100 | 0b0000 | 0b0111      | 0b000  | RW       | DBGVCR32_EL2       | DBGVCR32_EL2       |
| 0b100 | 0b1001 | 0b0000      | 0b000  | RW       | BRBCR_EL2          | BRBCR_EL2          |
| 0b100 | 0b1001 | 0b1101      | 0b011  | RW       | SPMACCESSR_EL2     | SPMACCESSR_EL2     |
| 0b101 | 0b1001 | 0b0000      | 0b000  | RW       | BRBCR_EL12         | BRBCR_EL1          |
| 0b101 | 0b1001 | 0b1101      | 0b011  | RW       | SPMACCESSR_EL12    | SPMACCESSR_EL1     |
| 0b110 | 0b1001 | 0b1101      | 0b011  | RW       | SPMACCESSR_EL3     | SPMACCESSR_EL3     |
| 0b110 | 0b1001 | 0b1110      | 0b111  | RW       | SPMROOTCR_EL3      | SPMROOTCR_EL3      |
| 0b111 | 0b1001 | 0b1110      | 0b111  | RW       | SPMSCR_EL1         | SPMSCR_EL1         |