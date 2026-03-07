## D1.7 Realm attestation flows

## D1.7.1 Attestation token generation flow

The following diagram shows the flow for a Realm to obtain an attestation token.

The Realm first calls RSI\_ATTESTATION\_TOKEN\_INIT, providing a challenge value. The output values include an upper bound on the attestation token size.

The Realm then calls RSI\_ATTESTATION\_TOKEN\_CONTINUE, providing the address of a buffer where the next part of the attestation token will be written. This command is called in a loop, until the result is not RSI\_INCOMPLETE.

Figure D1.21: Attestation token generation flow

<!-- image -->

See also:

- [A7.2.2 Attestation token generation](rmm-A7.2.md#a722-attestation-token-generation)
- [B5.4.2 RSI\_ATTESTATION\_TOKEN\_CONTINUE command](rmm-B5.4.2.md)
- [B5.4.3 RSI\_ATTESTATION\_TOKEN\_INIT command](rmm-B5.4.3.md)

## D1.7.2 Handling interrupts during attestation token generation flow

The following diagram shows how interrupts are handled during generation of an attestation token.

If the RMM detects that a physical interrupt is pending during execution of RSI\_ATTESTATION\_TOKEN\_CONTINUE, it saves the execution context to the REC object, and performs a REC exit due to IRQ.

During handling of the IRQ, the Host may signal a virtual interrupt to the REC.

On the next entry to the REC, if a virtual interrupt is pending, it is taken to the REC's exception vector.

Whether or not a virtual interrupt was taken, on return to the original thread, the REC determines that X0 is RSI\_INCOMPLETE, and therefore calls RSI\_ATTESTATION\_TOKEN\_CONTINUE again.

<!-- image -->

Figure D1.22: Attestation token generation with interrupt handling flow

<!-- image -->

## See also:

- [A4.3.5 REC exit due to IRQ](rmm-A4.3.md#a435-rec-exit-due-to-irq)
- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A7.2.2 Attestation token generation](rmm-A7.2.md#a722-attestation-token-generation)
- [B5.4.2 RSI\_ATTESTATION\_TOKEN\_CONTINUE command](rmm-B5.4.2.md)
- [B5.4.3 RSI\_ATTESTATION\_TOKEN\_INIT command](rmm-B5.4.3.md)
- [D1.3.1 Realm entry and exit flow](rmm-D1.3.md#d131-realm-entry-and-exit-flow)