import unittest

Login = __import__("MFSCRM_log_in")
Edit_Customer = __import__("MFSCRM_Edit_Customer")
Customer_Summary = __import__("MFSCRM_Customer_summary")
Delete_Customer = __import__("MFSCRM_Delete_customer")
Add_product = __import__("MFSCRM_Add_product")
Edit_Product = __import__("MFSCRM_Edit_Product")
Delete_Product = __import__("MFSCRM_Delete_Product")
Add_Service = __import__("MFSCRM_Delete_Service")
Edit_Service = __import__("MFSCRM_Edit_Service")
Delete_Service = __import__("MFSCRM_Delete_Service")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Login))
suite.addTests(loader.loadTestsFromModule(Edit_Customer))
suite.addTests(loader.loadTestsFromModule(Customer_Summary))
suite.addTests(loader.loadTestsFromModule(Delete_Customer))
suite.addTests(loader.loadTestsFromModule(Add_product))
suite.addTests(loader.loadTestsFromModule(Edit_Product))
suite.addTests(loader.loadTestsFromModule(Delete_Product))
suite.addTests(loader.loadTestsFromModule(Add_Service))
suite.addTests(loader.loadTestsFromModule(Edit_Service))
suite.addTests(loader.loadTestsFromModule(Delete_Service))



runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

