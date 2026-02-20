## D22.3 Validity of SME and SVE state

- IVBJBR The Effective value of PSTATE.SM and the value of PSTATE.ZA configure whether SME architectural state is valid and accessible.
- IWFHKZ CPACR\_EL1.SMEN, CPTR\_EL2.{TSM, SMEN}, and CPTR\_EL3.ESM configure whether SME-related instructions can be executed or are trapped.
- IKKFXN SMCR\_ELx.EZT0 configures whether SME2 instructions that access the ZT0 register can be executed or are trapped.
- RXCCXW The controls for trapping SME-related instructions and the controls for the validity of SME architectural state are independent.
- IJGRTR Because the trap and architectural state validity are controlled independently, the following scenarios are all permissible:
- Instructions trap, state invalid.
- -For example, an OS traps the first usage of SME-related instructions by a process.
- Instructions trap, state valid.
- -For example, a process was running with valid SME architectural state and an OS configures traps to detect when the next usage of SME architectural state occurs.
- -Enabling the trap does not affect or corrupt the SME architectural state.
- Instructions permitted, state invalid.
- -For example, a process is permitted to execute SME-related instructions but is currently not running in Streaming SVE mode . SMEdata-processing instructions which access SVE vector or predicate registers are illegal and are trapped, but SVE instructions operate on the Non-streaming SVE register state. The process can execute an SMSTART instruction to enter Streaming SVE mode .
- -For example, a process is running in Streaming SVE mode , but has not enabled access to the ZA storage. SMEinstructions that access ZA are illegal and are trapped, but the process can execute an SMSTART instruction to enable access to the ZA storage.
- Instructions permitted, state valid.
- -For example, a process is running in Streaming SVE mode , and has enabled access to ZA storage.