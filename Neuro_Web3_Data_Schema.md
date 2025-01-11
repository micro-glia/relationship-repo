# Neuro Web3 Data Schema

This document defines the core data structures for storing and processing neuroscience data in a blockchain context. It specifies the field types, validation rules, and example JSON objects for three key data models.

---

## 1. Data Models

### 1.1 Participant Data
- **Schema**
  - **id**: Unique identifier for each participant. (*Type*: String, *Validation*: UUID format)
  - **name**: Participant's full name. (*Type*: String, *Validation*: 3-50 characters)
  - **email**: Email address of the participant. (*Type*: String, *Validation*: Standard email format)
  - **consent**: Indicates whether the participant has given consent. (*Type*: Boolean, *Validation*: Must be true)
- **Example JSON**
  ```json
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "consent": true
  }

### 1.2 Neuroscience Data
- **Description**: Schema for neuroscience-specific data such as EEG and MRI files.
- **Fields**:
  - `data_id` (string): A unique identifier for the data entry.
  - `participant_id` (string): The ID of the participant providing the data.
  - `data_type` (string): Type of neuroscience data (e.g., EEG, MRI).
  - `timestamp` (ISO_8601 timestamp): When the data was collected.
  - `data_file` (file): A link or reference to the data file.
- **Validation Rules**:
  - `data_id`: Must be a valid UUID.
  - `data_type`: Must be one of `EEG`, `MRI`, or `fMRI`.
  - `data_file`: File must be less than 1GB and properly formatted.
- **Example JSON**:
  ```json
  {
    "data_id": "987e6543-e21b-12d3-a456-426614174000",
    "participant_id": "123e4567-e89b-12d3-a456-426614174000",
    "data_type": "EEG",
    "timestamp": "2025-01-10T22:00:00Z",
    "data_file": "https://example.com/data/eeg_file_001.edf"
  }


```markdown
### 1.3 Transaction Metadata
- **Description**: Schema for transaction-related metadata to track blockchain token integration.
- **Fields**:
  - `transaction_id` (string): A unique identifier for the transaction.
  - `participant_id` (string): The participant involved in the transaction.
  - `token_amount` (float): Amount of tokens involved in the transaction.
  - `timestamp` (ISO_8601 timestamp): When the transaction occurred.
  - `status` (string): The transaction status (e.g., `pending`, `completed`).
- **Validation Rules**:
  - `transaction_id`: Must be a valid UUID.
  - `token_amount`: Must be a positive number.
  - `status`: Must be one of `pending`, `completed`, or `failed`.
- **Example JSON**:
  ```json
  {
    "transaction_id": "567e1234-e89b-12d3-a456-426614174000",
    "participant_id": "123e4567-e89b-12d3-a456-426614174000",
    "token_amount": 10.5,
    "timestamp": "2025-01-10T23:00:00Z",
    "status": "completed"
  }


---

### Full Copy/Paste Workflow:
1. Start with **1.1 Participant Data**.
2. Add **1.2 Neuroscience Data** (block above).
3. Add **1.3 Transaction Metadata** (block above).
4. Complete your `.md` file with the remaining sections like **Validation Rules**, **API Integration**, and **How Schemas Enable Monetization Strategies**.

This structure ensures everything is broken into consistent, copy-paste-ready blocks. Let me know if you’d like further tweaks!

