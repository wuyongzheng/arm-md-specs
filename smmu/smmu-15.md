## Chapter 15 Translation procedure

The following flowcharts are an illustration of the sequence of events from the beginning of a translation to its final outcome. They represent an abstracted translation flow to summarize the information in the rest of this specification.

The purpose is to indicate the end result of different types of transactions, in terms of transaction and translation success or error responses (including PCIe ATS errors and completion responses). Certain aspects are not intended to be depicted in detail, including but not limited to:

- Atomic translation table update mechanism.
- TLB conflict, configuration cache conflict (which might happen at an IMPLEMENTATION DEFINED point in the translation).
- Speculative operations (which do not record errors or faults).
- Attribute control.
- Reporting of the events controlled by the SMMU\_CR2.REC\_CFG\_ATS field.

## 15.1 Translation procedure charts

Figure 15.1: Translation Procedure Chart 1

<!-- image -->

Figure 15.2: Translation Procedure Chart 2

<!-- image -->

Figure 15.3: Translation Procedure Chart 3

<!-- image -->

Figure 15.4: Translation Procedure Chart 4

<!-- image -->

Figure 15.5: Translation Procedure Chart 5

<!-- image -->

Chapter 15. Translation procedure 15.2. Notes on translation procedure charts

<!-- image -->

Figure 15.6: Translation Procedure Chart 6

## 15.2 Notes on translation procedure charts

For every fault or termination that an ordinary transaction might experience, an ATS Translation Request has an equivalent defined response.

Similarly, an ATS Translated transaction might experience a subset of the fault or termination reasons.

Generally, situations that represent a configuration error result in a Completer Abort (CA) response to the endpoint, situations that represent an explicit prevention or disable of ATS service result in an Unsupported Request (UR) response, and Translation-related failures result in a successful Translation Completion having R == W == 0 (that is, no access for this address).

See section 3.9.1.2 Responses to ATS Translation Requests .