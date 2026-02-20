## H4.2 DCC and ITR registers

The DCC comprises data transfer registers , the DTRs, and associated flow-control flags. The data transfer registers are DTRRXand DTRTX.

The ITR comprises a single register, EDITR, and associated flow-control flags.

In AArch64 state, software can access the data transfer registers as:

- Areceive and transmit pair for 32-bit full duplex operation:
- -The write-only DBGDTRTX\_EL0 register to transmit data.
- -The read-only DBGDTRRX\_EL0 register to receive data.
- Asingle 64-bit read/write register, DBGDTR\_EL0, for 64-bit half-duplex operation.
- The read/write OSDTRTX\_EL1 and OSDTRRX\_EL1 registers for save and restore.

In AArch32 state, software can access the data transfer registers only as:

- Areceive and transmit pair, for 32-bit full duplex operation:
- -The write-only DBGDTRTXint register to transmit data.
- -The read-only DBGDTRRXint register to receive data.
- The read/write DBGDTRTXext and DBGDTRRXext registers for save and restore.

The data transfer registers are also accessible by the external debug interface as a pair of 32-bit registers, DBGDTRRX\_EL0 and DBGDTRTX\_EL0. Both registers are read/write, allowing both 32-bit full-duplex and 64-bit half-duplex operation.

The DCC flow-control flags are EDSCR.{RXfull, TXfull, RXO, TXU}:

- The RXfull and TXfull ready flags are used for flow-control and are visible to software in the Debug system registers in DCCSR.
- The RX overrun flag, RXO, and the TX underrun flag, TXU, report flow-control errors.
- The flow-control flags are also accessible by software as simple read/write bits for saving and restoring over a powerdown when the OS Lock is locked in DSCR.
- The flow-control flags are accessible from the external debug interface in EDSCR.

Figure H4-1 shows the System register and external debug interface views of the EDSCR and DTR registers in both AArch64 state and AArch32 state. These figures do not include the save and restore views.

Figure H4-1 System register and external debug interface views of EDSCR and DTR registers, Normal access mode

<!-- image -->

EDITR and the ITR flow-control flags, EDSCR.{ITE, ITO} are accessible only by the external debug interface:

- The EDITR specifies an instruction to execute in Debug state.
- The ITR empty flag, ITE, is used for flow-control.
- The ITR overrun flag, ITO, reports flow-control errors.

Figure H4-2 External debug interface views of EDSCR and EDITR registers, Normal access mode

<!-- image -->

The sticky overflow flag, EDSCR.ERR, is used by both the DCC and ITR to report flow-control errors.

To save and restore the DCC registers for an external debugger over powerdown, software uses:

- The MDSCR\_EL1, OSDTRTX\_EL1, and OSDTRRX\_EL1 registers in AArch64 state.
- The DBGDSCRext, DBGDTRTXext, and DBGDTRRXext registers in AArch32 state.

Note

There is no save and restore mechanism for the ITR registers as the ITR is used only in Debug state.

Figure H4-3 System register views of EDSCR and DTR registers for save and restore

<!-- image -->