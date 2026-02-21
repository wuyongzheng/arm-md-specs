## Chapter 11 Debug/Trace

The SMMU architecture does not require the provision of debug support features. An implementation might provide its own debug features, subject to the following constraints:

- If an implementation supports Secure state, then a Non-secure or Realm debug agent must not be able to access any facilities related to Secure transaction handling.
- If an implementation supports Realm state, then a Non-secure or Secure debug agent must not be able to access any facilities related to Realm transaction handling.
- If an implementation supports the Root programming interface, then any agent not associated with Root state must not be able to access any facilities related to Root state.

Arm recommends that an implementation provides an IMPLEMENTATION DEFINED mechanism to read the contents of translation and configuration cache structures. If such a mechanism is provided, then it must not violate the general Security state constraints described above.