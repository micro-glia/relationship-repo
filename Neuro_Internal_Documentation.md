# Neuro Web3 Project: Internal Documentation

## 1. Validation Rules
### Participant Data Validation
- `participant_id`: Must be a valid UUID.
- `age`: Must be a positive integer between 18 and 100.
- `email`: Must match the regex pattern for valid emails.

### Neuroscience Data Validation
- `data_type`: Must be one of `EEG`, `MRI`, `fMRI`.
- `data_file`: Must be less than 1GB and use proper file extensions (`.edf`, `.nii`, etc.).

### Transaction Metadata Validation
- `transaction_id`: Must be a valid UUID.
- `token_amount`: Must be a positive float.

---

## 2. API Integration
### Endpoints Mapped to Schemas
- **GET /api/v1/participant**:
  - Fetch participant data using `participant_id`.
- **POST /api/v1/data**:
  - Submit neuroscience data validated against the `Neuroscience Data` schema.
- **GET /api/v1/token**:
  - Retrieve transaction metadata validated against the `Transaction Metadata` schema.

### Example API Workflow
1. User submits neuroscience data via **POST /api/v1/data**.
2. Backend validates data and stores it.
3. Upon success, a token transaction is created and logged via **Transaction Metadata**.

---

## 3. How Schemas Enable Monetization Strategies
### Example Monetization Flow
- **Data Access via Tokens**:
  - Neuroscience data stored using the **Neuroscience Data** schema is tokenized.
  - Researchers pay tokens (validated with the `Transaction Metadata` schema) to access specific datasets.
- **Premium Features**:
  - Participants can upgrade to premium features, verified with the `Participant Data` schema.


