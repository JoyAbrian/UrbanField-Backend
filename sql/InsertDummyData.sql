USE urban_fields;

-- Insert dummy data for users
INSERT INTO users (username, password, user_document, role) VALUES
    ('admin_user', 'admin_password', NULL, 'admin'),
    ('customer1', 'customer_password1', NULL, 'customer'),
    ('customer2', 'customer_password2', NULL, 'customer'),
    ('john_doe', 'john_password', NULL, 'customer'),
    ('jane_smith', 'jane_password', NULL, 'customer'),
    ('alice_jones', 'alice_password', NULL, 'customer'),
    ('bob_smith', 'bob_password', NULL, 'customer'),
    ('charlie_brown', 'charlie_password', NULL, 'customer'),
    ('david_cole', 'david_password', NULL, 'customer'),
    ('emily_davis', 'emily_password', NULL, 'customer'),
    ('frank_thomas', 'frank_password', NULL, 'customer'),
    ('grace_miller', 'grace_password', NULL, 'customer'),
    ('henry_wilson', 'henry_password', NULL, 'customer'),
    ('isabella_scott', 'isabella_password', NULL, 'customer'),
    ('jacob_lee', 'jacob_password', NULL, 'customer'),
    ('kate_harris', 'kate_password', NULL, 'customer'),
    ('leo_robinson', 'leo_password', NULL, 'customer'),
    ('mia_nguyen', 'mia_password', NULL, 'customer'),
    ('nathan_king', 'nathan_password', NULL, 'customer'),
    ('olivia_clark', 'olivia_password', NULL, 'customer');

-- Insert dummy data for field types
INSERT INTO field_types (name) VALUES
    ('Futsal'),
    ('Badminton');

-- Insert dummy data for fields
