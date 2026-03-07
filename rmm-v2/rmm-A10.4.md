## A10.4 Planes interrupts

- On REC creation, the GIC owner for the REC is P0.
- On Plane entry, P0 can transfer GIC ownership to the target Pn.
- On Plane entry, if P0 transfers GIC ownership to the target Pn then the GIC state in RsiPlaneEnter is ignored. This means that the GIC state of the owner is preserved and is shared across GIC ownership changes between planes.
- Allowing P0 to control which Plane is the GIC owner supports software usage models including the following:
- P0 is the GIC owner, and P0 emulates a vGIC for Pn, similar to how the Host emulates a vGIC for the Realm.
- P0 is a lightweight 'Pn switcher', which does not emulate a vGIC. GIC ownership is transferred to the Pn which contains the main Realm guest OS.
- P0 can read the value of ICH\_VTR\_EL2 using the RSI\_REALM\_CONFIG command.
- On Plane exit, P0 is the GIC owner. If GIC ownership was transferred to Pn on Plane entry, it returns to P0 on Plane exit.
- On Plane exit, Pn's GIC state is exposed to P0 via the RsiPlaneExit object.
- On REC entry the GIC state provided by the Host is assigned to the GIC owner.
- On REC entry, if the values of ICH\_LR\_EL2 describe one or more Pending interrupts and the most recent REC exit was from a Plane which is not the GIC owner then control returns to P0. This results in a Plane exit due to IRQ. RQZFYT On REC entry, if all of the following is true then control returns to P0, resulting in a Plane exit due to IRQ: · The most recent REC exit was from Pn · The most recent REC exit was not from the GIC owner · The value of ICH\_MISR\_EL2 at the time of the REC exit was not zero. IGJRBD On REC exit, the Realm GIC state of the GIC owner Plane is reported to the Host. RHCKNY During execution of a Plane which is not the GIC owner, direct injection of interrupts is masked. UJLJKV Direct injection of interrupts can be masked by setting ICH\_HCR\_EL2.DVIM = 1 .
- During execution of the GIC owner Plane, it is IMPLEMENTATION DEFINED whether direct injection of interrupts is masked.

See also:

- [A2.4.2 REC attributes](rmm-A2.4.md#a242-rec-attributes)
- [A4.1 Realm exception model overview](rmm-A4.1.md)
- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A10.2.3.2 Plane exit due to IRQ](rmm-A10.2.md#a10232-plane-exit-due-to-irq)
- [B5.4.13 RSI\_PLANE\_ENTER command](rmm-B5.4.13.md)
- [B5.4.16 RSI\_REALM\_CONFIG command](rmm-B5.4.16.md)