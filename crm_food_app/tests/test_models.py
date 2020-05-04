from crm_food_app.models import *

from django.test import TestCase


class RoleTestCase(TestCase):
    # Role Test
    def setUp(self):
        print('Setup Role Activity')
        self.role = Role.objects.create(name='waiter')

    def test_role_into(self):
        self.assertEqual(self.role.name, 'waiter')


class UserTestCase(TestCase):
    # User test

    def setUp(self):
        print('User Test Activity')
        self.role = Role.objects.create(name='waiter')
        self.user = User.objects.create(name='Tomas', surname='John',
                                        login='tom',email='tomasjohn@example.com',
                                        role=self.role,phone=5566778899)

    def test_user_into(self):
        self.assertEqual(self.user.name, 'Tomas')


class StatusTestCase(TestCase):
    # StatusTest

    def setUp(self):
        print('Setup Status Activity')
        self.status = Status.objects.create(name='inprogress')

    def test_status_into(self):
        self.assertEqual(self.status.name, 'inprogress')


class TableTestCase(TestCase):
    # Table Test
    def setUp(self):
        print('Setup Table Activity')
        self.table = Table.objects.create(name='Table№1')

    def test_table_into(self):
        self.assertEqual(self.table.name, 'Table№1')


class DepartmentTestCase(TestCase):
    # Department Test
    def setUp(self):
        print('Setup Department Activity')
        self.department = Department.objects.create(name='kitchen')

    def test_department_into(self):
        self.assertEqual(self.department.name, 'kitchen')


class MealCategoryTestCase(TestCase):
    # MealCategory Test

    def setUp(self):
        print('Setup MealCategory Activity')
        self.department = Department.objects.create(name='kitchen')
        self.mealcategory = MealCategory.objects.create(name='meat', department=self.department)

    def test_department_into(self):
        self.assertEqual(self.mealcategory.name, 'meat')


class MealTestCase(TestCase):
    # Meal Test

    def setUp(self):
        print("Setup Meal Activity")
        self.department = Department.objects.create(name='kitchen')
        self.mealcategory = MealCategory.objects.create(name='meat',
                                                        department=self.department)
        self.meal = Meal.objects.create(name='plov',
                                        category=self.mealcategory,
                                        price=250, description='some text')

    def test_meal_into(self):
        self.assertEqual(self.meal.name,'plov')


class OrderTestCase(TestCase):
    # Order Test

    def setUp(self):
        print("Setup Order Activity")
        self.role = Role.objects.create(name='waiter')
        self.user = User.objects.create(name='Tomas', surname='John',
                                        login='tom', email='tomasjohn@example.com',
                                        role=self.role, phone=5566778899)
        self.table = Table.objects.create(name='Table№1')
        self.order = Order.objects.create(waiter=self.user, table=self.table,
                                          isitopen=True)

    def test_order_into(self):
        self.assertEqual(self.order.isitopen, True)


class MealOrderTestCase(TestCase):
    # MealOrder Test

    def setUp(self):
        print("Setup MealOrder Activity")
        self.role = Role.objects.create(name='waiter')
        self.user = User.objects.create(name='Tomas', surname='John',
                                        login='tom', email='tomasjohn@example.com',
                                        role=self.role, phone=5566778899)
        self.table = Table.objects.create(name='Table№1')
        self.order = Order.objects.create(waiter=self.user, table=self.table,
                                          isitopen=True)
        self.department = Department.objects.create(name='kitchen')
        self.mealcategory = MealCategory.objects.create(name='meat', department=self.department)
        self.meal = Meal.objects.create(name='plov',category=self.mealcategory,price=250)
        self.mealorder = MealOrder.objects.create(order=self.order, meal=self.meal,count=2)

    def test_mealorder_into(self):
        self.assertEqual(self.mealorder.count, 2)
