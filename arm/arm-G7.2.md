## G7.2 Organization of registers in the ( coproc == 0b1110 ) encoding space

The System registers in the ( coproc == 0b1110 ) encoding space provide a number of distinct control functions, covering:

- Debug.
- Trace.
- Execution environment control, for identification of the trivial Jazelle implementation.

Because these functions are distinct, the descriptions of these registers are distributed, as follows:

- In this manual, Debug registers describes the Debug registers.
- The Embedded Trace Macrocell Architecture Specification describes the Trace registers.

This section summarizes the allocation of the System registers in the ( coproc == 0b1110 ) encoding space between these different functions, and the register encodings in this space that are reserved.

The 32-bit System register encodings are classified by the { opc1 , CRn , opc2 , CRm } values required to access them using an MCR or an MRC instruction. The 64-bit System register encodings are classified by the { opc1 , CRm } values required to access them using an MCRR or an MRRC instruction. For the registers in the ( coproc == 0b1110 ) encoding space, the opc1 value determines the primary allocation of these registers, as follows:

opc1==0

Debug registers.

opc1==1

Trace registers.

opc1==7

Jazelle registers. Jazelle registers are implemented as required for a trivial Jazelle implementation.

Other opc1 values

Reserved.

Note

Primary allocation of ( coproc == 0b1110 ) register function by opc1 value differs from the allocation of ( coproc == 0b1111 ) registers, where primary allocation is by CRn value for 32-bit register accesses, or CRm value for 64-bit register accesses.

For the Debug and Jazelle registers, Table G7-1 defines:

- The { opc1 , CRn , opc2 , CRm } values used for accessing the 32-bit registers using the MRC and MCR instructions.
- The { opc1 , CRm } values used for accessing the 64-bit register using the MRRC instruction.

Some Debug registers can also be accessed using the LDC and STC instructions. Table G7-1 defines the CRn values used for accessing the registers using these instructions.

Note

The only permitted uses of the LDC and STC instructions are:

- An LDC access to load data from memory to DBGDTRTXint.
- An STC access to store data to memory from DBGDTRRXint.

In the LDC and STC syntax descriptions in this Manual, the required coproc value of p14 and CRn value of c5 are given explicitly.

## G7.2.1 Register access instruction arguments, ( coproc == 0b1110 ) registers

Table G7-1 shows the MCR , MRC , and MRRC instruction arguments required for accesses to each register that can be visible in the System register interface in the ( coproc == 0b1110 ) encoding.

Table G7-1

|   coproc |   opc1 |   CRn | CRm    | opc2    | Access   | Mnemonic      | Register      |
|----------|--------|-------|--------|---------|----------|---------------|---------------|
|     1110 |    000 |  0000 | 0000   | 000     | RO       | DBGDIDR       | DBGDIDR       |
|     1110 |    000 |  0000 | 0000   | 010     | RW       | DBGDTRRXext   | DBGDTRRXext   |
|     1110 |    000 |  0000 | 0001   | 000     | RO       | DBGDSCRint    | DBGDSCRint    |
|     1110 |    000 |  0000 | 0010   | 000     | RW       | DBGDCCINT     | DBGDCCINT     |
|     1110 |    000 |  0000 | 0010   | 010     | RW       | DBGDSCRext    | DBGDSCRext    |
|     1110 |    000 |  0000 | 0011   | 010     | RW       | DBGDTRTXext   | DBGDTRTXext   |
|     1110 |    000 |  0000 | 0101   | 000     | •        | DBGDTRRXint   | •             |
|     1110 |    000 |  0000 | 0101   | 000     | •        | DBGDTRTXint   | •             |
|     1110 |    000 |  0000 | 0110   | 000     | RW       | DBGWFAR       | DBGWFAR       |
|     1110 |    000 |  0000 | 0110   | 010     | RW       | DBGOSECCR     | DBGOSECCR     |
|     1110 |    000 |  0000 | 0111   | 000     | RW       | DBGVCR        | DBGVCR        |
|     1110 |    000 |  0000 | m[3:0] | 100     | RW       | DBGBVR<n>     | DBGBVR[]      |
|     1110 |    000 |  0000 | m[3:0] | 101     | RW       | DBGBCR<n>     | DBGBCR[]      |
|     1110 |    000 |  0000 | m[3:0] | 110     | RW       | DBGWVR<n>     | DBGWVR[]      |
|     1110 |    000 |  0000 | m[3:0] | 111     | RW       | DBGWCR<n>     | DBGWCR[]      |
|     1110 |    000 |  0001 | 0000   | 000     | RO       | DBGDRAR       | DBGDRAR       |
|     1110 |    000 |  0001 | 0000   | 100     | WO       | DBGOSLAR      | DBGOSLAR      |
|     1110 |    000 |  0001 | 0001   | 100     | RO       | DBGOSLSR      | DBGOSLSR      |
|     1110 |    000 |  0001 | 0011   | 100     | RW       | DBGOSDLR      | DBGOSDLR      |
|     1110 |    000 |  0001 | 0100   | 100     | RW       | DBGPRCR       | DBGPRCR       |
|     1110 |    000 |  0001 | m[3:0] | 001     | RW       | DBGBXVR<n>    | DBGBXVR[]     |
|     1110 |    000 |  0010 | 0000   | 000     | RO       | DBGDSAR       | DBGDSAR       |
|     1110 |    000 |  0111 | 0000   | 111     | RO       | DBGDEVID2     | DBGDEVID2     |
|     1110 |    000 |  0111 | 0001   | 111     | RO       | DBGDEVID1     | DBGDEVID1     |
|     1110 |    000 |  0111 | 0010   | 111     | RO       | DBGDEVID      | DBGDEVID      |
|     1110 |    000 |  0111 | 1000   | 110     | RW       | DBGCLAIMSET   | DBGCLAIMSET   |
|     1110 |    000 |  0111 | 1001   | 110     | RW       | DBGCLAIMCLR   | DBGCLAIMCLR   |
|     1110 |    000 |  0111 | 1110   | 110     | RO       | DBGAUTHSTATUS | DBGAUTHSTATUS |
|     1110 |    111 |  0000 | 0000   | 000     | RO       | JIDR          | JIDR          |
|     1110 |    111 |  0001 | 0000   | 000     | RO       | JOSCR         | JOSCR         |
|     1110 |    111 |  0010 | 0000   | 000     | RO       | JMCR          | JMCR          |
|     1110 |   0000 |  0001 | •      | DBGDRAR | •        |               |               |
|     1110 |   0000 |  0010 | •      | DBGDSAR | •        |               |               |

Table G7-2 shows the LDC and STC instruction arguments required for accesses to the Debug registers that can be accessed using these instructions.

Table G7-2 Mapping of LDC and STC instruction arguments to System registers

| Name        | CRn   | Instruction   | Description                                           |
|-------------|-------|---------------|-------------------------------------------------------|
| DBGDTRTXint | c5    | LDC           | Debug Data Transfer Register, Transmit, Internal View |
| DBGDTRRXint | c5    | STC           | Debug Data Transfer Register, Receive, Internal View  |

## Note

In the instruction syntax descriptions for the LDC and STC instructions, the required coproc and CRn values are given explicitly as coproc == p14 , CRn == c5 .