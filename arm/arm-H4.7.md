## H4.7 Pseudocode description of the operation of the DCC and ITR registers

The basic operation of the DCC and ITR registers is shown by the following pseudocode functions. These functions do not cover the behavior when OSLSR.OSLK == 1, meaning that the OS Lock is locked:

```
· Write_DBGDTR_EL0[] . · Write_DBGDTRRX_EL0[] . · Write_DBGDTRTX_EL0[] . · Write_EDITR[] . · CheckForDCCInterrupts() .
```

For the definition of the DTR Registers, see shared/debug/dccanditr/DTR.

## Chapter H5 The Embedded Cross-Trigger Interface

This chapter describes the Embedded Cross-Trigger interface. It contains the following sections:

- About the Embedded Cross-Trigger.
- Basic operation on the ECT.
- Cross-triggers on a PE in an Arm A-profile implementation.
- Description and allocation of CTI triggers.
- CTI registers programmers' model.
- Examples.