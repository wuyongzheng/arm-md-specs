## A5.5 VDEV mapping validation

- DNZSKS A VDEV mapping validation is a process via which the addresses and attributes of mappings to device memory are checked for consistency with values expected by the Realm.
- IFZHYH The outcome of a successful VDEV mapping validation is a change of RIPAS to RIPAS\_DEV.
- ILLPZR A VDEV mapping validation consists of actions taken first by the Realm, and then by the Host:
- The Realm issues a VDEV mapping validation request by executing RSI\_VDEV\_VALIDATE\_MAPPING.
- -The input values to RSI\_VDEV\_VALIDATE\_MAPPING include:
* The requested IPA range: [base,

top)

* The base of the expected PA range
* Flags which indicate the expected memory attributes
- -The RMM records these values in the REC, and then performs a REC exit due to VDEV mapping validation.
- In response, the Host executes zero or more RMI\_RTT\_DEV\_VALIDATE commands.

Output values from RSI\_VDEV\_VALIDATE\_MAPPING indicate:

- The top of the IPA range which has been modified by the command ( new\_base ).
- Whether the Host rejected the Realm request.

Output values from RSI\_VDEV\_VALIDATE\_MAPPING are expected to be handled by the Realm as follows:

SRCNJD

| new_base              | response            | Meaning                                                                                                                                           | Expected Realm action                                                                                                                                                                            |
|-----------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| new_base == base      | RSI_RESPONSE_ACCEPT | DRAFT VDEV mapping validation incomplete. VDEV mapping validation incomplete. VDEV mapping                                                        | Call the command again, with base = new_base . Call the command again, with base = new_base No further Realm action required. Depends on protocol agreed between Realm and Host, out of scope of |
| base < new_base < top | RSI_RESPONSE_ACCEPT |                                                                                                                                                   | .                                                                                                                                                                                                |
| new_base == top       | RSI_RESPONSE_ACCEPT | validation complete.                                                                                                                              |                                                                                                                                                                                                  |
| new_base == base      | RSI_RESPONSE_REJECT | VDEV mapping validation request rejected.                                                                                                         | this specification.                                                                                                                                                                              |
| base < new_base < top | RSI_RESPONSE_REJECT | VDEV mapping validation to partial region [base, new_base) . Host rejected request to validate device memory mapping for region [new_base, top) . | Depends on protocol agreed between Realm and Host, out of scope of this specification.                                                                                                           |

IYKKSX

The VDEV mapping validation process, together with the Realm Initial Measurement ensures that a Realm can always reliably determine the RIPAS of any Protected IPA.

- IYBJZF

A VDEV mapping validation is applied by one or more calls to the RMI\_RTT\_DEV\_VALIDATE command.

ITLRPR

Successful execution of RMI\_RTT\_DEV\_VALIDATE targets an RTTE at address rec.dev\_mem\_addr .

- IYVGNP page whose device memory mapping is to be validated:

On successful execution of RMI\_RTT\_DEV\_VALIDATE, all of the following are set to the address of the next

· rec.dev\_mem\_addr

ILDDPH

- rec.dev\_mem\_pa
- The command output value

ISGKTK On REC entry following a REC exit due to VDEV mapping validation, GPR values are updated to indicate for how much of the target IPA range the VDEV mapping validation request has been applied.

SMWWXS To complete a VDEV mapping validation for a given target IPA range, a Realm should execute RSI\_VDEV\_VALIDATE\_MAPPING in a loop, until the value of X1 reaches the top of the target IPA range.

- RFDCBZ On REC entry following a REC exit due to VDEV mapping validation, rec.dev\_mem\_response is set to the
- value of

enter.flags.dev\_mem\_response .

- If all of the following are true then the output value of RSI\_VDEV\_VALIDATE\_MAPPING indicates 'Host
- rejected the request':
- rec.dev\_mem\_addr is not equal to rec.dev\_mem\_top .
- rec.dev\_mem\_response is REJECT.

Otherwise, the output value of RSI\_VDEV\_VALIDATE\_MAPPING indicates 'Host accepted the request'.

## See also:

- A2.4.2 REC attributes
- A4.2 REC entry
- A4.3.13 REC exit due to VDEV mapping validation
- A5.2.2 Realm IPA state
- A7.1.1 Realm Initial Measurement
- Chapter A9 Realm device assignment
- B3.105 RecDevMemResponseToRsi function
- B4.5.51 RMI\_REC\_ENTER command
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command
- D1.5.3 RIPAS change flow

DRAFT