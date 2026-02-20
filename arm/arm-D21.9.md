## D21.9 MPAM errors

RDHSBM

An MPAM error is detected when a memory read, memory write, instruction fetch, or translation table walk results in one of:

- The PARTID is out-of-range . Either:
- -The PARTID is a physical PARTID and it exceeds MPAMIDR\_EL1.PARTID\_MAX.
- -The PARTID is treated as virtual and it exceeds (4 x MPAMIDR\_EL1.VPMR\_MAX) + 3.
- The PARTID is treated as virtual and the corresponding MPAMVPMV\_EL2.VPM\_V&lt;m&gt; valid flag indicates that a valid mapping does not exist.
- The PMG is out-of-range. The PMG exceeds MPAMIDR\_EL1.PMG\_MAX.

In some implementations, some MPAM errors might never occur. For example, an implementation with only w bits of PARTID and MPAMIDR\_EL1.PARTID\_MAX as (2 w - 1), and that truncates PARTID values with non-zero bits higher than w - 1, can never have a physical PARTID out-of-range error. See also:

- PARTID virtualization, for the definitions of out-of-range and treated as virtual .

## D21.9.1 Behavior when a PARTID is out-of-range

RYGRQN

When a physical or virtual PARTID from an MPAMn\_ELx.PARTID\_D or MPAMn\_ELx.PARTID\_I field is out-of-range , the behavior is a CONSTRAINED UNPREDICTABLE choice of:

- The out-of-range PARTID is replaced by any in-range PARTID.

- The out-of-range PARTID is replaced by the Default physical PARTID.

For the replacement PARTID space of a replacement PARTID, see PARTID space on error.

IDYBVB

See also:

- PARTID virtualization, for the definition of out-of-range .

## D21.9.2 Behavior when a valid mapping does not exist for a PARTID that is treated as virtual

RNHSJC

If a PARTID from an MPAMn\_ELx.PARTID\_D or MPAMn\_ELx.PARTID\_I field, or its replacement if that PARTID was out-of-range , is treated as virtual , and the corresponding MPAMVPMV\_EL2.VPM\_V&lt;m&gt; valid flag indicates that a valid mapping does not exist, the mapping for the Default virtual PARTID is used. If a valid mapping does not exist for the Default virtual PARTID, the Default physical PARTID is sent.

IFYYSQ

See also:

- PARTID virtualization, for the definitions of out-of-range and treated as virtual .

## D21.9.3 Behavior when a PMG is out-of-range

RVPZPD

When a PMG from an MPAMn\_ELx.PMG\_D or MPAMn\_ELx.PMG\_I field is out-of-range , the behavior is a CONSTRAINED UNPREDICTABLE choice of:

- The out-of-range PMG is replaced by any in-range PMG.
- The out-of-range PMG is replaced by the Default PMG.

## D21.9.4 PMG value when a Default PARTID is generated due to an MPAM error

RYBYMK

When the Default PARTID is generated due to an MPAM error, the PMG value is a CONSTRAINED UNPREDICTABLE choice of:

- MPAMn\_ELx.PMG\_D or MPAMn\_ELx.PMG\_I.
- The Default PMG.

## D21.9.5 PARTID space on error

RVYHDZ

An MPAM error does not change the PARTID space.

IDWCRN