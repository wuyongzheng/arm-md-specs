## D19.4 Branch record buffer

| I FBHCC   | The Branch record buffer can contain:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R KSLSM   | The Branch record buffer storage has a maximum number of Branch records as defined by BRBIDR0_EL1.NUMREC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I PPBZP   | The Branch record buffer provides System registers to access the Branch records stored in the Branch record buffer storage. These System registers provide access to up to 32 Branch records without the need for explicit synchronization between each System register read. When more than 32 Branch records are implemented, the Branch record buffer provides a banking mechanism to provide access to multiple banks, each bank containing up to 32 Branch records. BRBFCR_EL1.BANK controls which bank is currently selected, and updates to BRBFCR_EL1.BANK require explicit synchronization before accessing the bank. |
| R WLSWP   | Accessing Branch records 0-31 is performed by setting BRBFCR_EL1.BANK to 0b00 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R WRJLW   | Accessing Branch records 32-63 is performed by setting BRBFCR_EL1.BANK to 0b01 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R TJGLK   | The Branch record with index 0 is the youngest captured branch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R HTRNR   | The Branch record with index n is younger than Branch record with index n+1 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| R DTPDK   | On the generation of a new Branch record, if the Branch record buffer storage is full, then the oldest Branch record is lost.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| R SQLCX   | When the buffer contains M valid Branch records, where M > 0 and M is less than the maximum number of Branch records , all of the following are true: • Branch records with index 0 to M-1 are all valid. • All other Branch records are invalid.                                                                                                                                                                                                                                                                                                                                                                              |
| R PGDLX   | The creation of a Branch record is considered an indirect write to BRBTGT<n>_EL1, BRBSRC<n>_EL1 and BRBINF<n>_EL1, and therefore requires explicit synchronization before being read.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I SFFNF   | The generation of Branch records performs indirect reads and indirect writes of System registers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I KFYTV   | Synchronization requirements for AArch64 System registers defines the synchronization requirements for direct reads, direct writes, indirect reads, and indirect writes of System registers made by instructions and external agents.                                                                                                                                                                                                                                                                                                                                                                                          |

## D19.4.1 Invalidating the record buffer

RLLHYN Execution of BRB IALL causes all Branch records to be invalidated.

RPFRNW

ABranch record, R , is invalidated by the instruction BRB IALL , W , if all of the following are true:

- R is caused by a branch operation or exception, B .

- B is either:

- In program order before a Context synchronization event , CSE .

- Is the Context synchronization event .

- CSE is in program order before W .

RLWPKR

ABranch record R is not invalidated by the instruction BRB IALL , W , if all of the following are true:

- R is caused by a branch operation or exception, B .

- B is in program order after a Context synchronization event , CSE .

RWMZKF

RJSCWK

- CSE is in program order after W .

It is CONSTRAINED UNPREDICTABLE whether a Branch record R is invalidated by the instruction BRB IALL , W , if all of the following are true:

- CSE1 is in program order before W .
- R is caused by a branch operation or exception, B .
- B is in program order after a Context synchronization event , CSE1
- B is either:
- -In program order before a Context synchronization event , CSE2.
- -Is the Context synchronization event , CSE2.
- CSE2 is in program order after W and there are no other CSEs between CSE1 and CSE2.

If a Branch record is invalidated, all older Branch records are invalidated.

When a Branch record has been invalidated, it remains invalid until it is overwritten by any of the following:

- Anew Branch record is created.
- ABranch record is injected using the BRB INJ instruction.