# Neuro Token Economics

## Overview
The Neuro token serves as the core utility token for the neuroscience data platform. It is used to manage data access rights, incentivize participants, and enable governance. The token ensures seamless interaction between participants, researchers, and data providers within the Web3 ecosystem.

---

## Smart Contract Functions

### 1. Data Access Rights
**Function:** `grantAccess(address recipient, uint256 tokenId)`  
- **Description:** Allows the token holder to grant access to neuroscience data tied to a specific token.  
- **Parameters:**
  - `recipient`: The address of the user receiving access.
  - `tokenId`: The ID of the token tied to the data.  
- **Returns:** Confirmation of access granted.

---

### 2. Reward Distribution
**Function:** `distributeRewards(uint256 amount, address[] memory recipients)`  
- **Description:** Distributes rewards to participants contributing data or governance decisions.  
- **Parameters:**
  - `amount`: Total reward amount to be distributed.
  - `recipients`: List of participant addresses.  
- **Returns:** Success message.

---

### 3. Governance Mechanisms
**Function:** `vote(uint256 proposalId, uint256 voteWeight)`  
- **Description:** Allows token holders to vote on governance proposals.  
- **Parameters:**
  - `proposalId`: The ID of the proposal being voted on.
  - `voteWeight`: Number of tokens allocated to the vote.  
- **Returns:** Confirmation of vote submitted.

---

## Solidity Interface

Below is a Solidity interface that implements the core token functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface INeuroToken {
    // Data Access
    function grantAccess(address recipient, uint256 tokenId) external returns (bool);

    // Reward Distribution
    function distributeRewards(uint256 amount, address[] memory recipients) external returns (bool);

    // Governance
    function vote(uint256 proposalId, uint256 voteWeight) external returns (bool);
}

# Internal Documentation

## Validation Rules
- **Token Transfer Limits:**
  - Maximum of 10,000 tokens per transaction to prevent abuse.
- **Reward Issuance:**
  - Tokens distributed only upon verified data contributions.
- **Governance Participation:**
  - Only token holders with more than 1,000 tokens can vote on proposals.
- **Transaction Validation:**
  - Sender must have sufficient balance.
  - Transactions are processed on-chain for transparency.

## API Integration

### Reward Distribution API
- **Endpoint:** `POST /api/v1/reward`
- **Description:** Issues tokens to users for their contributions to the platform.
- **Payload Example:**
  {
    "user_id": "user123",
    "reward_amount": 100
  }

- **Response Example:**
  {
  "status": "success",
  "message": "Tokens successfully issued."
  }

### Governance Voting API

- **Endpoint:** `POST /api/v1/vote`
- **Description:** Allows users to cast their votes on proposals using tokens.
- **Payload Example:**
  {
  "proposal_id": 42,
  "support": true
  }
- **Response Example:**
  {
  "status": "success",
  "message": "Vote successfully recorded."
  }

### Retrieve Voting Results API

- **Endpoint:** GET /api/v1/vote/:proposalId
- **Description:** Retrieves the results of a specific governance proposal.
- **Response Example:**
  {
  "proposal_id": 42,
  "results": {
    "yes": 12000,
    "no": 8000
   }
  }

## Monetization Enablement

- Access Tokenization:
  - Researchers or organizations purchase tokens to access neuroscience data, creating a direct revenue stream.
- Reward Mechanisms:
  - Encourages sustained platform participation by rewarding contributors.
- Governance Mechanisms:
  - Attracts investors by aligning platform decisions with token holder interests.
