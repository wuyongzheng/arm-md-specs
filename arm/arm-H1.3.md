## H1.3 Required debug authentication

Any implementation must provide the debug authentication defined in this section, which controls:

- Whether the PE can halt.
- Whether some aspects of non-invasive debug are permitted.
- Some legacy aspects of the AArch32 self-hosted debug model.

The pseudocode functions shown in Table H1-1, and the conditions that follow that table, define the architectural requirements for debug authentication.

Table H1-1 Debug authentication functions

| Pseudocode function                                      | Description                                                              |
|----------------------------------------------------------|--------------------------------------------------------------------------|
| ExternalNoninvasiveDebugEnabled()                        | Returns TRUE if Non-secure non-invasive debug is enabled.                |
| ExternalInvasiveDebugEnabled()                           | Returns TRUE if Non-secure invasive debug is enabled.                    |
| ExternalSecureNoninvasiveDebugEnabled()                  | Returns TRUE if Secure non-invasive debug is enabled.                    |
| AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() | Returns TRUE if Secure invasive self-hosted debug is enabled in AArch32. |
| ExternalSecureInvasiveDebugEnabled()                     | Returns TRUE if Secure invasive debug is enabled.                        |
| ExternalRealmNoninvasiveDebugEnabled()                   | Returns TRUE if Realm non-invasive debug is enabled.                     |
| ExternalRealmInvasiveDebugEnabled()                      | Returns TRUE if Realm invasive debug is enabled.                         |
| ExternalRootNoninvasiveDebugEnabled()                    | Returns TRUE if Root non-invasive debug is enabled.                      |
| ExternalRootInvasiveDebugEnabled()                       | Returns TRUE if Root invasive debug is enabled.                          |

## The following conditions always apply:

- If ExternalInvasiveDebugEnabled() is FALSE then ExternalSecureInvasiveDebugEnabled() is FALSE.
- If ExternalNoninvasiveDebugEnabled() is FALSE then ExternalSecureNoninvasiveDebugEnabled() is FALSE.
- If ExternalInvasiveDebugEnabled() is TRUE then ExternalNoninvasiveDebugEnabled() is TRUE.
- If ExternalSecureInvasiveDebugEnabled() is TRUE then ExternalSecureNoninvasiveDebugEnabled() is TRUE.

## If FEAT\_Debugv8p4 is implemented:

- ExternalNoninvasiveDebugEnabled() always returns TRUE.
- ExternalSecureNoninvasiveDebugEnabled() returns the same as ExternalSecureInvasiveDebugEnabled() .

## If FEAT\_RME is implemented, the following additional conditions always apply:

- If ExternalInvasiveDebugEnabled () is FALSE then ExternalRealmInvasiveDebugEnabled() is FALSE.
- If any of ExternalInvasiveDebugEnabled() , ExternalSecureNoninvasiveDebugEnabled() , or ExternalRealmInvasiveDebugEnabled () are FALSE, then ExternalRootInvasiveDebugEnabled() is FALSE.
- ExternalRealmNoninvasiveDebugEnabled() returns the same as ExternalRealmInvasiveDebugEnabled() .

- ExternalRootNoninvasiveDebugEnabled() returns the same as ExternalRootInvasiveDebugEnabled() .

If FEAT\_RME is not implemented, ExternalSecureInvasiveDebugEnabled () determines whether halting is prohibited or allowed at EL3. If FEAT\_RME is implemented, ExternalRootInvasiveDebugEnabled () determines whether halting is prohibited or allowed at EL3.

Arm recommends the use of the interface described in Recommended authentication interface to provide this debug authentication. The pseudocode functions in A-profile Architecture Pseudocode, which are linked to by the entries in the Pseudocode function column of Table H1-1, assume that this interface is implemented.

## Chapter H2 Debug State

This chapter describes Debug state. It contains the following sections:

- About Debug state.
- Halting the PE on debug events.
- Entering Debug state.
- Behavior in Debug state.
- Exiting Debug state.

Note

Table K14-1 disambiguates the general register references used in this chapter.