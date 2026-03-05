"""
ORM Script for testing User model and superuser operations
Run with: python manage.py shell < core_app/scripts/accounts_orm.py
"""

from django.contrib.auth import get_user_model

User = get_user_model()

print("\n" + "="*60)
print("USER ORM TEST SCRIPT")
print("="*60)

# 1. Create a new user
print("\n1. Creating a new user...")
user1 = User.objects.create_user(
    email='user1@example.com',
    password='password123',
    name='John Doe'
)
print(f"   ✓ User created: {user1.email} (ID: {user1.id})")
print(f"   - Name: {user1.name}")
print(f"   - Is Staff: {user1.is_staff}")
print(f"   - Is Active: {user1.is_active}")

# 2. Create another user
print("\n2. Creating another user...")
user2 = User.objects.create_user(
    email='user2@example.com',
    password='password456',
    name='Jane Smith'
)
print(f"   ✓ User created: {user2.email} (ID: {user2.id})")

# 3. Check total users
print("\n3. Total users in database:")
total_users = User.objects.count()
print(f"   ✓ Total: {total_users} users")

# 4. Retrieve a user
print("\n4. Retrieving a user by email...")
retrieved_user = User.objects.get(email='user1@example.com')
print(f"   ✓ Retrieved: {retrieved_user.name} ({retrieved_user.email})")

# 5. Update a user
print("\n5. Updating a user...")
retrieved_user.name = 'John Updated'
retrieved_user.save()
print(f"   ✓ Updated: {retrieved_user.name}")

# 6. List all users
print("\n6. All users in database:")
all_users = User.objects.all()
for user in all_users:
    print(f"   - {user.email} | {user.name} | Staff: {user.is_staff}")

# 7. Create superuser
print("\n7. Creating a superuser...")
try:
    superuser = User.objects.create_superuser(
        email='admin@example.com',
        password='adminpass123',
        name='Admin User'
    )
    print(f"   ✓ Superuser created: {superuser.email}")
    print(f"   - Is Staff: {superuser.is_staff}")
    print(f"   - Is Superuser: {superuser.is_superuser}")
except Exception as e:
    print(f"   ✗ Error creating superuser: {e}")

# 8. Verify superuser
print("\n8. Verifying superuser...")
try:
    admin = User.objects.get(email='admin@example.com')
    print(f"   ✓ Is Staff: {admin.is_staff}")
    print(f"   ✓ Is Superuser: {admin.is_superuser}")
    print(f"   ✓ Has Permissions: {admin.has_perm('auth.add_user')}")
except:
    print(f"   - Superuser not found")

print("\n" + "="*60)
print("ORM TEST COMPLETED SUCCESSFULLY!")
print("="*60 + "\n")    