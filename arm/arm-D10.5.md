## D10.5 Allocation Tag Access controls

IGJZWR

RYLWMV

Allocation Tag Access is used for all of the following:

- Determining access to Allocation Tags in memory.
- Enabling Tag Checking of memory accesses.
- By instructions inserting Logical Address Tags into addresses.

The following table shows the System register controls that are used to enable Allocation Tag Access :

## Table D10-1 Allocation Tag Access controls

| Exception level   | System register controls                 |
|-------------------|------------------------------------------|
| EL3               | SCTLR_EL3.ATA                            |
| EL2               | SCR_EL3.ATA, SCTLR_EL2.ATA               |
| EL1               | SCR_EL3.ATA, HCR_EL2.ATA, SCTLR_EL1.ATA  |
| EL0               | SCR_EL3.ATA, HCR_EL2.ATA, SCTLR_ELx.ATA0 |

RCWPLR

When executed at an Exception level where Allocation Tag Access is disabled, instructions that insert Logical Address Tags into addresses treat the Allocation Tag used to generate the Logical Address Tag as zero.

SYHLJC

Arm recommends that when software requires access to Allocation Tags in a context but Tag Checking is not required, the SCTLR\_ELx.{TCF, TCF0} field affecting that context is set to 0b00 . For more information, see Tag Check Faults.