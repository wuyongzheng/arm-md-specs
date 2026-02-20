## K9.1 Using Memory access mode in AArch64 state

Figure K9-1 and Figure K9-2 show the processes for using Memory access mode to implement a download (external host to target) and an upload (target to external host).

To transfer n words of data:

- The download sequence needs n +6 accesses by the external debug interface.
- The upload sequence needs n +8 accesses by the external debug interface.

In both cases, in the innermost loop the debugger can make an external access to a DTR without polling EDSCR after each write as underrun and overrun detection prevent failure. Normally external accesses from the debugger are outpaced by the memory accesses of the PE, making underruns and overruns unlikely. If this is not the case, the EDSCR.ERR flag is set to 1. This is checked once at the end of the sequence, although a debugger can check it more often, for example once for each page. If the EDSCR.ERR flag is set to 1 because of overrun or underrun, the debugger can restart. The address to restart from is frozen in X0. EDSCR.ERR might also be set because of a Data Abort.

If underruns and overruns are common, the debugger can pace itself accordingly.

Note

- The base address must be a multiple of 4.
- The order of the writes that set up the address does not matter in Debug state.

Figure K9-1 Fast code download in AArch64 state (external host to target)

<!-- image -->

In Figure K9-1, the sequence for the fast code download is as follows:

1. Setup. From the external debug interface:
- a. Write address [31:0] to DBGDTRRX\_EL0.
- b. Write address [63:32] to DBGDTRTX\_EL0.
- c. Write MRS X0, DBGDTR\_EL0 to EDITR. The PE executes this instruction.
- d. Set EDSCR.MA to 1.
2. Loop n times. From the external debug interface:
- a. Write to DBGDTRRX\_EL0. The PE reads the word from DTRRX and stores it to memory. It increments X0 by 4.
3. Epilogue. From the external debug interface:
- a. Clear EDSCR.MA to 0.
- b. Read EDSCR to check for overruns or Data Aborts during download.

Figure K9-2 Fast data upload in AArch64 state (target to external host)

<!-- image -->

In Figure K9-2, the sequence for the fast code download is as follows:

1. Setup. From the external debug interface:
- a. Write address [31:0] to DBGDTRRX\_EL0.
- b. Write address [63:32] to DBGDTRTX\_EL0.
- c. Write MRS X0, DBGDTR\_EL0 to EDITR.
- d. Write MSR DBGDTR\_EL0, X0 to EDITR. This dummy operation ensures EDSCR.TXfull == 1.
- e. Set EDSCR.MA to 1.
- f. Read DBGDTRTX\_EL0 and discard the value. The PE returns the previous DTR value, loads the first word, and writes it to DTR. It increments X0 by 4.
2. Loop n -1 times. From the external debug interface:
- a. Read DBGDTRTX\_EL0. The PE returns the previous DTRTX value, loads a new word, and writes it to DTRTX. It increments X0 by 4.

3. Epilogue. From the external debug interface:
- a. Clear EDSCR.MA to 0.
- b. Read DBGDTRTX\_EL0 for the n th value.
- c. Read EDSCR to check for underruns, overruns or Data Aborts during upload.

## Appendix K10 Software Usage Examples

This appendix gives Software usage examples, for cases where these are likely to contribute significantly to an understanding of the Arm architecture.

It contains the following sections:

- Use of the Advanced SIMD complex number instructions.
- Use of the Armv8.2 extensions to the Cryptographic Extension.
- SVE and SVE2 Programming Examples.
- Use of the FEAT\_PCDPHINT STSHH and PRFM IR (immediate) hint instructions.
- Use of the Embedded Trace and Trace Buffer Extensions.
- Use of the GCS Extension.
- Use of the RAS Extension.
- Example OS Save and Restore sequences.