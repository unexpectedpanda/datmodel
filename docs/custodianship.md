---
hide:
  - footer
---

# Custodianship

Making the schema publicly available and providing a stable, available pathway to updating
that schema is a challenge when you consider the timescales involved might stretch to
decades, given the longevity of the LogiqX DAT format.

The following guidelines attempt to provide this stability and continuous stewardship over
the schema, with full recognition that entropy and divergence are highly likely.

## Parties involved

*  **Schema lead**. A nominated figurehead. The schema lead's primary role is to
   facilitate discussions and to break stalemates in voting.

*  **Git repository admins**. These members manage the repository and updating of the
   publicly available schema.

*  **Schema custodians**. These members make decisions around changes to the schema.
    Custodians are made up of long-term invested individuals, maintainers of client
    software that processes DAT files, maintainers of databases that generate DAT files,
    and Git repository admins.

## Schema hosting and management

1.  The schema is hosted in a public Git repository.

1.  The repository must be managed by at least two active Git repository admins.

    1.  If an admin is inactive for more than six months, their position is considered
        void and they accept that they will be replaced and their permissions removed from
        the repository.

    1.  A replaced admin may return to become an additional admin if they parted on good
        terms with known reasons for their absence. Admins who disappear for more than
        six months without notice may not return without significant justification.

1.  A pull request requires at least one approval from a person who is not the author of
    the pull request.

1.  Git repository admins accept the agreed-upon decisions of custodians and the schemas
    they develop, regardless of personal involvement.

## Schema proposal process

1.  Anyone can propose an update to the schema through a public pull request or issue, but
    that proposal must come with the following:

    1.  A compelling justification.

    1.  An understanding that greater weight is given to proposals made by the following:

        * Known larger groups who release DAT files.

        * Maintainers of consequential client software that processes DAT files.

    1.  An understanding that changes impact how end clients might process a DAT file, and
        that those changes might not be adopted by end clients or the groups that release
        DAT files.

    1.  An understanding that the proposal could be rejected.

1.  The decision process to accept or reject a proposal starts when a custodian replies to
    the proposal, indicating the proposal is under discussion.

1.  The discussion and voting on the decision has a time limit of 45 days.

1.  The discussion happens in public on the proposal, although deeper context might happen
    in other channels. Dissenting opinions are important as a matter of record, in case
    the proposal needs to be revisited in the future.

1.  The steps for the discussion should be as follows:

    1.  Ignore any proposed implementation at first. Instead, define the root issue the
        proposal is trying to address.

    1.  With the root issue in mind, is the proposal in scope for the schema?

    1.  If the proposal is in scope, start from the angle of trying to make it work. How
        do we properly solve for the root issue? What are the sensible defaults? How do we
        keep optionality to a minimum?

    1.  With this in mind, develop a preview schema to address the proposal.

    1.  Is the impact of the preview schema on client software and database maintainers
        acceptable?

1.  The conduct of custodians during a discussion should be as follows:

    1.  Assume good intent from all parties involved.

    1.  Make a sincere effort to understand other points of view. A useful framework for
        resolving differences can be to honestly engage with the question: "what would
        have to be true to accept this?".

    1.  When in doubt, put the community needs first, not the feelings or personal
        investment of the custodian, or the amount of work required to implement the
        change.

    1.  Refrain from heated or snide language, and refrain from personal attacks.
        Don't attempt to publicly undermine other custodians.

    1.  After a majority vote has been made, the issue is considered resolved, with all
        parties moving forward and accepting the result.

1.  A decision requires a simple majority vote to pass.

    1.  Custodians can vote to accept or reject the proposal, or abstain from the vote.

    1.  A custodian who fails to vote within 45 days has their vote counted as an
        abstention, regardless of circumstance.

    1.  A vote stalemate is broken by the schema lead. The schema lead has up to 15 days
        beyond the the initial 45 day time limit to resolve the stalemate. Upon failure to
        resolve the stalemate, the proposal is rejected.

1.  The decision on whether to accept or reject the proposal is posted publicly on the
    proposal by a nominated custodian, with an appropriate justification. If the proposal
    is accepted, an updated preview schema is provided.

1.  Upon accepting a proposal, a new schema version is submitted by custodians as a pull
    request. Old schema versions remain online for compatibility with older DAT files.

1.  A new proposal that seeks to address the same root issue as a rejected proposal won't
    be considered until at least 12 months after the initial rejection.

