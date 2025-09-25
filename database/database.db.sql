BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "business_costs" (
	"id"	INTEGER,
	"cost_number"	VARCHAR(50) NOT NULL UNIQUE,
	"category_id"	INTEGER NOT NULL,
	"cost_description"	VARCHAR(255) NOT NULL,
	"cost_date"	DATE NOT NULL,
	"due_date"	DATE,
	"supplier_id"	INTEGER,
	"employee_id"	INTEGER,
	"invoice_number"	VARCHAR(50),
	"taxable_amount"	DECIMAL(10, 2) NOT NULL,
	"vat_rate"	DECIMAL(5, 2) DEFAULT 0.00 CHECK("vat_rate" >= 0 AND "vat_rate" <= 100),
	"vat_amount"	DECIMAL(10, 2) DEFAULT 0.00,
	"total_amount"	DECIMAL(10, 2) NOT NULL,
	"payment_status"	VARCHAR(10) DEFAULT 'pending' CHECK("payment_status" IN ('pending', 'paid', 'overdue')),
	"payment_date"	DATE,
	"notes"	VARCHAR(500) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "financial_categories"("id"),
	FOREIGN KEY("employee_id") REFERENCES "employees"("id"),
	FOREIGN KEY("supplier_id") REFERENCES "providers"("id"),
	CHECK("supplier_id" IS NULL OR "employee_id" IS NULL),
	CHECK("total_amount" = "taxable_amount" + "vat_amount")
);
CREATE TABLE IF NOT EXISTS "business_revenues" (
	"id"	INTEGER,
	"revenue_number"	VARCHAR(50) NOT NULL UNIQUE,
	"category_id"	INTEGER NOT NULL,
	"revenue_description"	VARCHAR(255) NOT NULL,
	"revenue_date"	DATE NOT NULL,
	"due_date"	DATE,
	"client_id"	INTEGER,
	"employee_id"	INTEGER,
	"invoice_number"	VARCHAR(50),
	"taxable_amount"	DECIMAL(10, 2) NOT NULL,
	"vat_rate"	DECIMAL(5, 2) DEFAULT 0.00 CHECK("vat_rate" >= 0 AND "vat_rate" <= 100),
	"vat_amount"	DECIMAL(10, 2) DEFAULT 0.00,
	"total_amount"	DECIMAL(10, 2) NOT NULL,
	"payment_status"	VARCHAR(10) DEFAULT 'pending' CHECK("payment_status" IN ('pending', 'received', 'overdue')),
	"payment_date"	DATE,
	"notes"	VARCHAR(500) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "financial_categories"("id"),
	FOREIGN KEY("client_id") REFERENCES "clients"("id"),
	FOREIGN KEY("employee_id") REFERENCES "employees"("id"),
	CHECK("client_id" IS NULL OR "employee_id" IS NULL),
	CHECK("total_amount" = "taxable_amount" + "vat_amount")
);
CREATE TABLE IF NOT EXISTS "clients" (
	"id"	INTEGER,
	"client_code"	VARCHAR(20) NOT NULL UNIQUE,
	"first_name"	VARCHAR(50) NOT NULL,
	"last_name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(100) CHECK("email" IS NULL OR ("email" GLOB '*@*.*' AND length("email") >= 5 AND length("email") <= 100 AND "email" NOT GLOB '*@*@*' AND "email" NOT GLOB '.*@*' AND "email" NOT GLOB '*@.*')),
	"phone"	VARCHAR(20) CHECK("phone" IS NULL OR (length("phone") >= 8 AND length("phone") <= 20 AND ("phone" GLOB '+[0-9]*' OR "phone" GLOB '[0-9]*') AND "phone" NOT GLOB '*[a-zA-Z]*')),
	"client_address"	VARCHAR(255),
	"city"	VARCHAR(100),
	"postal_code"	VARCHAR(10),
	"country"	VARCHAR(50) DEFAULT 'Italy',
	"birth_date"	DATE,
	"gender"	VARCHAR(10) CHECK("gender" IS NULL OR "gender" IN ('M', 'F', 'Other')),
	"tax_code"	VARCHAR(20),
	"vat_number"	VARCHAR(20),
	"client_category"	VARCHAR(20) DEFAULT 'standard' CHECK("client_category" IN ('standard', 'premium', 'vip', 'business')),
	"client_status"	VARCHAR(20) DEFAULT 'active' CHECK("client_status" IN ('active', 'inactive', 'suspended', 'blocked')),
	"marketing_consent"	BOOLEAN DEFAULT 0,
	"newsletter_consent"	BOOLEAN DEFAULT 0,
	"sms_consent"	BOOLEAN DEFAULT 0,
	"privacy_consent"	BOOLEAN DEFAULT 1,
	"consent_date"	DATETIME,
	"registration_date"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"last_visit_date"	DATETIME,
	"last_purchase_date"	DATETIME,
	"total_purchases"	DECIMAL(10, 2) DEFAULT 0.00,
	"visit_count"	INTEGER DEFAULT 0,
	"notes"	VARCHAR(2000),
	"registered_by"	INTEGER,
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("registered_by") REFERENCES "employees"("id")
);
CREATE TABLE IF NOT EXISTS "counter_departments" (
	"id"	INTEGER,
	"counter_code"	VARCHAR(20) NOT NULL UNIQUE,
	"counter_name_en"	VARCHAR(100) NOT NULL,
	"counter_name_it"	VARCHAR(100) NOT NULL,
	"counter_description"	VARCHAR(255),
	"is_weighable"	BOOLEAN DEFAULT 0,
	"requires_refrigeration"	BOOLEAN DEFAULT 0,
	"display_order"	INTEGER DEFAULT 0,
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "employee_contracts" (
	"id"	INTEGER,
	"employee_id"	INTEGER NOT NULL UNIQUE,
	"contract_number"	VARCHAR(50) NOT NULL UNIQUE,
	"contract_type"	VARCHAR(20) NOT NULL CHECK("contract_type" IN ('permanent', 'temporary', 'apprenticeship', 'internship', 'consultant')),
	"contract_start_date"	DATE NOT NULL,
	"contract_end_date"	DATE,
	"job_title"	VARCHAR(100),
	"weekly_hours"	INTEGER DEFAULT 40,
	"hourly_rate"	DECIMAL(8, 2),
	"monthly_salary"	DECIMAL(10, 2),
	"annual_salary"	DECIMAL(10, 2),
	"trial_period_days"	INTEGER DEFAULT 90,
	"notice_period_days"	INTEGER DEFAULT 30,
	"vacation_days_per_year"	INTEGER DEFAULT 20,
	"sick_leave_days_per_year"	INTEGER DEFAULT 10,
	"contract_level"	VARCHAR(100),
	"ccnl_type"	VARCHAR(50),
	"benefits"	VARCHAR(1000) DEFAULT '',
	"notes"	VARCHAR(1000) DEFAULT '',
	"is_active"	BOOLEAN DEFAULT 1,
	"contract_signed_date"	DATE,
	"contract_renewed_date"	DATE,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("employee_id") REFERENCES "employees"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "employees" (
	"id"	INTEGER,
	"employee_code"	VARCHAR(20) NOT NULL UNIQUE,
	"first_name"	VARCHAR(50) NOT NULL,
	"last_name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(100) NOT NULL CHECK("email" GLOB '*@*.*' AND length("email") >= 5 AND length("email") <= 100 AND "email" NOT GLOB '*@*@*' AND "email" NOT GLOB '.*@*' AND "email" NOT GLOB '*@.*') UNIQUE,
	"personal_email"	VARCHAR(100) CHECK("personal_email" IS NULL OR ("personal_email" GLOB '*@*.*' AND length("personal_email") >= 5 AND length("personal_email") <= 100 AND "personal_email" NOT GLOB '*@*@*' AND "personal_email" NOT GLOB '.*@*' AND "personal_email" NOT GLOB '*@.*')),
	"phone"	VARCHAR(20) CHECK("phone" IS NULL OR (length("phone") >= 8 AND length("phone") <= 20 AND "phone" GLOB '+*[0-9]*')),
	"personal_phone"	VARCHAR(20) CHECK("personal_phone" IS NULL OR (length("personal_phone") >= 8 AND length("personal_phone") <= 20 AND "personal_phone" GLOB '+*[0-9]*')),
	"hire_date"	DATE NOT NULL,
	"location_id"	INTEGER,
	"salary"	DECIMAL(10, 2),
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("location_id") REFERENCES "locations"("id")
);
CREATE TABLE IF NOT EXISTS "financial_categories" (
	"id"	INTEGER,
	"category_code"	VARCHAR(20) NOT NULL UNIQUE,
	"category_name"	VARCHAR(100) NOT NULL,
	"category_scope"	VARCHAR(10) NOT NULL CHECK("category_scope" IN ('cost', 'revenue', 'both')),
	"category_type"	VARCHAR(15) NOT NULL,
	"periodicity"	VARCHAR(15) CHECK("periodicity" IS NULL OR "periodicity" IN ('daily', 'weekly', 'monthly', 'quarterly', 'semi-annual', 'yearly')),
	"category_description"	VARCHAR(255) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "keycloak_sessions" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"session_id"	VARCHAR(255) NOT NULL UNIQUE,
	"access_token_hash"	VARCHAR(128),
	"expires_at"	DATETIME NOT NULL,
	"ip_address"	VARCHAR(45),
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "locations" (
	"id"	INTEGER,
	"location_code"	VARCHAR(20) NOT NULL UNIQUE,
	"location_name"	VARCHAR(100) NOT NULL,
	"location_type"	VARCHAR(30) NOT NULL DEFAULT 'store' CHECK("location_type" IN ('store', 'warehouse', 'office', 'headquarters', 'distribution_center')),
	"location_address"	VARCHAR(255) NOT NULL,
	"city"	VARCHAR(100) NOT NULL,
	"postal_code"	VARCHAR(10),
	"country_code"	VARCHAR(3) NOT NULL,
	"region_state"	VARCHAR(100),
	"phone"	VARCHAR(20) CHECK("phone" IS NULL OR (length("phone") >= 8 AND length("phone") <= 20 AND "phone" GLOB '+*[0-9]*')),
	"email"	VARCHAR(254) CHECK("email" IS NULL OR ("email" GLOB '*@*.*' AND length("email") >= 5 AND length("email") <= 254 AND "email" NOT GLOB '*@*@*' AND "email" NOT GLOB '.*@*' AND "email" NOT GLOB '*@.*')),
	"opening_time"	TIME DEFAULT '08:00:00',
	"closing_time"	TIME DEFAULT '20:00:00',
	"is_active"	BOOLEAN DEFAULT 1,
	"notes"	VARCHAR(500) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "loyalty_cards" (
	"id"	INTEGER,
	"client_id"	INTEGER NOT NULL UNIQUE,
	"card_number"	VARCHAR(20) NOT NULL UNIQUE,
	"card_status"	VARCHAR(20) DEFAULT 'active' CHECK("card_status" IN ('active', 'inactive', 'blocked', 'expired')),
	"points"	INTEGER DEFAULT 0 CHECK("points" >= 0),
	"points_earned"	INTEGER DEFAULT 0 CHECK("points_earned" >= 0),
	"points_used"	INTEGER DEFAULT 0 CHECK("points_used" >= 0),
	"points_expires_at"	DATETIME,
	"card_tier"	VARCHAR(20) DEFAULT 'bronze' CHECK("card_tier" IN ('bronze', 'silver', 'gold', 'platinum')),
	"issue_date"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"card_expiry_date"	DATETIME,
	"last_used_date"	DATETIME,
	"total_transactions"	INTEGER DEFAULT 0,
	"total_spent"	DECIMAL(10, 2) DEFAULT 0.00,
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("client_id") REFERENCES "clients"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "products" (
	"id"	INTEGER,
	"product_code"	VARCHAR(20) NOT NULL UNIQUE,
	"product_variant"	VARCHAR(50),
	"product_name"	VARCHAR(255) NOT NULL,
	"product_description"	VARCHAR(1000) DEFAULT '',
	"weight_volume"	VARCHAR(50),
	"department_id"	INTEGER,
	"counter_id"	INTEGER,
	"supplier_id"	INTEGER,
	"barcode"	VARCHAR(50) UNIQUE,
	"plu_code"	VARCHAR(20),
	"unit_of_measure"	VARCHAR(20) NOT NULL DEFAULT 'pcs',
	"product_class"	VARCHAR(50),
	"classification"	VARCHAR(100),
	"checkout_method"	VARCHAR(20) CHECK("checkout_method" IN ('BARCODE', 'SCALE', 'MANUAL')),
	"consumption_flag"	VARCHAR(20),
	"target_margin"	DECIMAL(5, 2),
	"selling_price"	DECIMAL(10, 2),
	"labeling_requirements"	VARCHAR(500),
	"photo_data"	BLOB,
	"photo_filename"	VARCHAR(255),
	"photo_mime_type"	VARCHAR(50),
	"photo_size"	INTEGER,
	"sva_sale_active"	BOOLEAN DEFAULT 0,
	"sva_max_quantity"	INTEGER,
	"sva_loyalty_required"	BOOLEAN DEFAULT 0,
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"updated_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("counter_id") REFERENCES "counter_departments"("id"),
	FOREIGN KEY("department_id") REFERENCES "supermarket_departments"("id"),
	FOREIGN KEY("supplier_id") REFERENCES "providers"("id")
);
CREATE TABLE IF NOT EXISTS "providers" (
	"id"	INTEGER,
	"provider_code"	VARCHAR(20) NOT NULL UNIQUE,
	"provider_name"	VARCHAR(100) NOT NULL,
	"provider_type"	VARCHAR(20) DEFAULT 'supplier' CHECK("provider_type" IN ('supplier', 'delivery')),
	"contact_person"	VARCHAR(100),
	"contact_info"	VARCHAR(255),
	"email"	VARCHAR(100) CHECK("email" IS NULL OR ("email" GLOB '*@*.*' AND length("email") >= 5 AND length("email") <= 100 AND "email" NOT GLOB '*@*@*' AND "email" NOT GLOB '.*@*' AND "email" NOT GLOB '*@.*')),
	"phone"	VARCHAR(20) CHECK("phone" IS NULL OR (length("phone") >= 8 AND length("phone") <= 20 AND ("phone" GLOB '+[0-9]*' OR "phone" GLOB '[0-9]*') AND "phone" NOT GLOB '*[a-zA-Z]*')),
	"provider_address"	VARCHAR(255),
	"city"	VARCHAR(100),
	"postal_code"	VARCHAR(10),
	"country"	VARCHAR(50) DEFAULT 'Italy',
	"vat_number"	VARCHAR(20),
	"tax_code"	VARCHAR(20),
	"website"	VARCHAR(255),
	"payment_terms_days"	INTEGER DEFAULT 30,
	"discount_percentage"	DECIMAL(5, 2) DEFAULT 0.00,
	"notes"	VARCHAR(1000) DEFAULT '',
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "roles" (
	"id"	INTEGER,
	"role_name"	VARCHAR(50) NOT NULL UNIQUE,
	"role_description"	VARCHAR(255) DEFAULT '',
	"role_level"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "stock_movement_items" (
	"id"	INTEGER,
	"stock_movement_id"	INTEGER NOT NULL,
	"product_id"	INTEGER NOT NULL,
	"quantity_ordered"	DECIMAL(10, 3),
	"quantity_actual"	DECIMAL(10, 3) NOT NULL,
	"unit_cost"	DECIMAL(10, 2),
	"unit_price"	DECIMAL(10, 2),
	"discount_amount"	DECIMAL(10, 2) DEFAULT 0.00,
	"discount_percent"	DECIMAL(5, 2) DEFAULT 0.00,
	"line_subtotal"	DECIMAL(12, 2),
	"line_total"	DECIMAL(12, 2),
	"tax_rate"	DECIMAL(5, 2) DEFAULT 0.00,
	"batch_number"	VARCHAR(50),
	"items_expiry_date"	DATE,
	"line_notes"	VARCHAR(500) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	UNIQUE("stock_movement_id","product_id"),
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	FOREIGN KEY("stock_movement_id") REFERENCES "stock_movements"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "stock_movements" (
	"id"	INTEGER,
	"movement_number"	VARCHAR(50) NOT NULL UNIQUE,
	"movement_type"	VARCHAR(20) NOT NULL CHECK("movement_type" IN ('purchase', 'sale', 'adjustment', 'transfer', 'loss', 'return')),
	"movement_direction"	VARCHAR(3) NOT NULL CHECK("movement_direction" IN ('IN', 'OUT')),
	"provider_id"	INTEGER,
	"loyalty_card_id"	INTEGER,
	"employee_id"	INTEGER NOT NULL,
	"movement_date"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"due_date"	DATETIME,
	"delivery_date"	DATETIME,
	"movement_status"	VARCHAR(20) DEFAULT 'completed' CHECK("movement_status" IN ('pending', 'completed', 'verified', 'paid', 'disputed', 'cancelled')),
	"payment_method"	VARCHAR(20) CHECK("payment_method" IN ('bank_transfer', 'cash', 'card', 'mixed', 'check', 'credit', 'voucher_payment', 'other')),
	"cash_received"	DECIMAL(10, 2),
	"change_given"	DECIMAL(10, 2) DEFAULT 0.00,
	"subtotal"	DECIMAL(12, 2),
	"discount_total"	DECIMAL(10, 2) DEFAULT 0.00,
	"tax_total"	DECIMAL(10, 2) DEFAULT 0.00,
	"final_total"	DECIMAL(12, 2),
	"payment_terms"	VARCHAR(255),
	"notes"	VARCHAR(1000) DEFAULT '',
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("employee_id") REFERENCES "employees"("id"),
	FOREIGN KEY("loyalty_card_id") REFERENCES "loyalty_cards"("id"),
	FOREIGN KEY("provider_id") REFERENCES "providers"("id"),
	CHECK(("movement_type" = 'sale' AND "loyalty_card_id" IS NOT NULL) OR ("movement_type" != 'sale')),
	CHECK(("movement_type" = 'purchase' AND "provider_id" IS NOT NULL) OR ("movement_type" != 'purchase')),
	CHECK(("movement_type" = 'sale' AND "payment_method" IS NOT NULL) OR ("movement_type" != 'sale'))
);
CREATE TABLE IF NOT EXISTS "supermarket_departments" (
	"id"	INTEGER,
	"department_code"	VARCHAR(20) NOT NULL UNIQUE,
	"department_name"	VARCHAR(100) NOT NULL,
	"department_type"	VARCHAR(20) DEFAULT 'standard' CHECK("department_type" IN ('frozen', 'fresh', 'dry', 'beverages', 'cleaning', 'personal_care', 'standard')),
	"parent_department_id"	INTEGER,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("parent_department_id") REFERENCES "supermarket_departments"("id")
);
CREATE TABLE IF NOT EXISTS "user_permissions" (
	"id"	INTEGER,
	"permission_name"	VARCHAR(100) NOT NULL CHECK("permission_name" GLOB '*.*') UNIQUE,
	"permission_description"	VARCHAR(255) DEFAULT '',
	"required_role_level"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"keycloak_user_id"	VARCHAR(255) NOT NULL UNIQUE,
	"username"	VARCHAR(100) NOT NULL,
	"email"	VARCHAR(100) NOT NULL CHECK("email" GLOB '*@*.*' AND length("email") >= 5 AND length("email") <= 100 AND "email" NOT GLOB '*@*@*' AND "email" NOT GLOB '.*@*' AND "email" NOT GLOB '*@.*') UNIQUE,
	"first_name"	VARCHAR(100),
	"last_name"	VARCHAR(100),
	"role_id"	INTEGER NOT NULL DEFAULT 4,
	"is_active"	BOOLEAN DEFAULT 1,
	"created_at"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("role_id") REFERENCES "roles"("id")
);
INSERT INTO "business_costs" VALUES (1,'COST-2024-001',1,'Affitto locali panetteria - Settembre 2024','2024-09-01','2024-09-15',NULL,NULL,'AFFITTO-092024',2500,0,0,2500,'paid','2024-09-10','Pagamento affitto mensile','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (2,'COST-2024-002',2,'Energia elettrica - Agosto 2024','2024-09-05','2024-09-25',1,NULL,'EE-082024-001',450,22,99,549,'pending',NULL,'Bolletta energia elettrica','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (3,'COST-2024-003',3,'Stipendi dipendenti - Agosto 2024','2024-08-31','2024-09-05',NULL,NULL,'STIPENDI-082024',8500,0,0,8500,'paid','2024-09-01','Pagamento stipendi mensili','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (4,'COST-2024-004',9,'Fornitura farina tipo 00 - 500kg','2024-09-10','2024-09-30',2,NULL,'FARINA-092024-15',680,4,27.2,707.2,'pending',NULL,'Fornitura materie prime','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (5,'COST-2024-005',9,'Prodotti lattiero-caseari freschi','2024-09-12','2024-09-22',3,NULL,'LATTE-092024-08',385.5,4,15.42,400.92,'pending',NULL,'Fornitura settimanale','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (6,'COST-2024-006',5,'Volantini promozionali autunno','2024-09-08','2024-09-20',4,NULL,'STAMPA-092024-03',320,22,70.4,390.4,'paid','2024-09-15','Materiale pubblicitario','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (7,'COST-2024-007',10,'Prodotti igiene e pulizia','2024-09-11','2024-09-25',1,NULL,'PULIZIA-092024-02',145.6,22,32.03,177.63,'pending',NULL,'Detergenti e disinfettanti','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (8,'COST-2024-008',6,'Riparazione forno principale','2024-09-14','2024-09-30',5,NULL,'RIP-FORNO-092024',780,22,171.6,951.6,'pending',NULL,'Manutenzione straordinaria','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (9,'COST-2024-009',7,'Polizza responsabilità civile - Rinnovo','2024-09-01','2024-09-15',NULL,NULL,'ASSICUR-2024-RC',1200,22,264,1464,'paid','2024-09-05','Rinnovo annuale polizza','2025-09-25 14:38:17');
INSERT INTO "business_costs" VALUES (10,'COST-2024-010',8,'IVA trimestrale - Q2 2024','2024-09-16','2024-09-16',NULL,NULL,'IVA-Q2-2024',2850,0,0,2850,'paid','2024-09-16','Versamento IVA trimestrale','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (1,'REV-2024-001',11,'Vendite giornaliere prodotti alimentari','2024-09-15',NULL,NULL,NULL,NULL,1250,4,50,1300,'received','2024-09-15','Incasso vendite giornaliere','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (2,'REV-2024-002',12,'Vendite prodotti da forno freschi','2024-09-15',NULL,NULL,NULL,NULL,680,4,27.2,707.2,'received','2024-09-15','Pane, dolci e prodotti da forno','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (3,'REV-2024-003',13,'Vendite bevande e caffetteria','2024-09-15',NULL,NULL,NULL,NULL,290,22,63.8,353.8,'received','2024-09-15','Bar e caffetteria','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (4,'REV-2024-004',14,'Servizio catering matrimonio','2024-09-12','2024-09-27',1,NULL,'CAT-092024-15',2800,10,280,3080,'pending',NULL,'Catering evento privato','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (5,'REV-2024-005',15,'Consegne a domicilio - Settimana 37','2024-09-13',NULL,NULL,NULL,NULL,420,22,92.4,512.4,'received','2024-09-13','Servizio delivery settimanale','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (6,'REV-2024-006',11,'Fornitura bar centrale - Ordine settimanale','2024-09-10','2024-09-30',2,NULL,'FORN-092024-22',1560,4,62.4,1622.4,'pending',NULL,'Cliente business ricorrente','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (7,'REV-2024-007',12,'Prodotti da forno ristorante "Da Mario"','2024-09-11','2024-10-01',3,NULL,'REST-092024-08',890,4,35.6,925.6,'pending',NULL,'Fornitura pane quotidiana','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (8,'REV-2024-008',12,'Torte personalizzate - Ordini speciali','2024-09-14',NULL,NULL,NULL,NULL,450,10,45,495,'received','2024-09-14','Dolci su commissione','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (9,'REV-2024-009',16,'Consulenza ricette tradizionali','2024-09-08','2024-09-30',4,NULL,'CONS-092024-01',800,22,176,976,'pending',NULL,'Servizio consulenza specialistica','2025-09-25 14:38:17');
INSERT INTO "business_revenues" VALUES (10,'REV-2024-010',11,'Riepilogo vendite settimana 36','2024-09-09',NULL,NULL,NULL,NULL,3200,4,128,3328,'received','2024-09-09','Incassi consolidati settimana precedente','2025-09-25 14:38:17');
INSERT INTO "clients" VALUES (1,'CLI001','Mario','Rossi','mario.rossi@gmail.com','+39123456789','Via Roma 123','Roma','00100','Italy','1985-03-15','M','RSSMRA85C15H501Z',NULL,'standard','active',1,1,0,1,'2024-01-10 10:00:00','2025-09-25 14:37:58','2024-09-15','2024-09-15',145.5,8,NULL,1,1,'2024-01-10','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (2,'CLI002','Anna','Bianchi','anna.bianchi@outlook.com','+39234567890','Via Milano 456','Milano','20100','Italy','1990-07-22','F','BNCNNA90L62F205K',NULL,'premium','active',1,1,1,1,'2024-01-12 14:30:00','2025-09-25 14:37:58','2024-09-18','2024-09-18',285.75,12,NULL,1,1,'2024-01-12','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (3,'CLI003','Giuseppe','Verdi','giuseppe.verdi@libero.it','+39345678901','Via Napoli 789','Napoli','80100','Italy','1978-11-08','M','VRDGPP78S08F839E',NULL,'vip','active',1,1,1,1,'2024-01-05 09:15:00','2025-09-25 14:37:58','2024-09-19','2024-09-19',520.3,15,NULL,2,1,'2024-01-05','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (4,'CLI004','Laura','Neri','laura.neri@yahoo.it','+39456789012','Via del Corso 321','Roma','00187','Italy','1992-02-14','F','NRELRA92B54H501X',NULL,'standard','active',0,1,0,1,'2024-01-15 16:45:00','2025-09-25 14:37:58','2024-09-10','2024-09-10',89.25,5,NULL,2,1,'2024-01-15','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (5,'CLI005','Roberto','Ferrari','roberto.ferrari@tiscali.it','+39567890123','Via Torino 25','Torino','10100','Italy','1988-09-30','M','FRRRRT88P30L219Q',NULL,'business','active',1,0,0,1,'2024-02-01 11:20:00','2025-09-25 14:37:58','2024-09-17','2024-09-17',1250.8,20,NULL,3,1,'2024-02-01','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (6,'CLI006','Sara','Conti','sara.conti@alice.it','+39678901234','Via Venezia 15','Venezia','30100','Italy','1995-12-03','F','CNTSRA95T43L736Y',NULL,'premium','active',1,1,1,1,'2024-02-10 13:00:00','2025-09-25 14:37:58','2024-09-16','2024-09-16',198.4,9,NULL,1,1,'2024-02-10','2025-09-25 14:37:58');
INSERT INTO "clients" VALUES (7,'CLI007','Francesco','Russo','francesco.russo@gmail.com','+39789012345','Via Firenze 88','Firenze','50100','Italy','1982-06-18','M','RSSFNC82H18D612W',NULL,'standard','inactive',0,0,0,1,'2024-03-01 15:30:00','2025-09-25 14:37:58','2024-08-20','2024-08-20',67.15,3,NULL,2,0,'2024-03-01','2025-09-25 14:37:58');
INSERT INTO "counter_departments" VALUES (1,'BAKERY','Bakery','Panetteria','Fresh bread and baked goods',0,0,1,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (2,'DELI','Delicatessen','Gastronomia','Ready-to-eat foods and specialties',1,1,2,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (3,'MEAT','Butcher','Macelleria','Fresh meat and poultry',1,1,3,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (4,'FISH','Fish Counter','Pescheria','Fresh fish and seafood',1,1,4,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (5,'CHEESE','Cheese Counter','Banco Formaggi','Fresh cheese and dairy',1,1,5,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (6,'PRODUCE','Produce','Ortofrutta','Fresh fruits and vegetables',1,0,6,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (7,'GROCERY','Grocery','Alimentari','Packaged food items',0,0,7,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (8,'FROZEN','Frozen Foods','Surgelati','Frozen products',0,1,8,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (9,'BEVERAGE','Beverages','Bevande','Drinks and beverages',0,0,9,1,'2025-09-25 14:38:08');
INSERT INTO "counter_departments" VALUES (10,'HOUSEHOLD','Household','Casa e Pulizia','Cleaning and household items',0,0,10,1,'2025-09-25 14:38:08');
INSERT INTO "employee_contracts" VALUES (1,1,'CT001','permanent','2023-01-15',NULL,'Store Manager',40,NULL,3500,42000,90,30,20,10,NULL,'CCNL Commercio','Health insurance, company car','',1,NULL,NULL,'2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "employee_contracts" VALUES (2,2,'CT002','permanent','2023-03-20',NULL,'Cashier',35,NULL,1800,21600,90,30,20,10,NULL,'CCNL Commercio','Health insurance, meal vouchers','',1,NULL,NULL,'2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "employee_contracts" VALUES (3,3,'CT003','temporary','2023-06-10',NULL,'Stock Clerk',40,NULL,2000,24000,90,30,20,10,NULL,'CCNL Commercio','Health insurance','',1,NULL,NULL,'2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "employee_contracts" VALUES (4,4,'CT004','permanent','2023-09-01',NULL,'Sales Assistant',30,NULL,1900,22800,90,30,20,10,NULL,'CCNL Commercio','Health insurance, meal vouchers','',1,NULL,NULL,'2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "employee_contracts" VALUES (5,5,'CT005','permanent','2024-01-10',NULL,'Administrative Assistant',40,NULL,2800,33600,90,30,20,10,NULL,'CCNL Terziario','Health insurance, flexible hours','',1,NULL,NULL,'2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "employees" VALUES (1,'EMP001','Mario','Rossi','mario.rossi@dbsmartapi.com','mario.rossi@gmail.com','+390123456789','+393351234567','2023-01-15',1,3500,1,'2025-09-25 14:37:46');
INSERT INTO "employees" VALUES (2,'EMP002','Giulia','Bianchi','giulia.bianchi@dbsmartapi.com','giulia.bianchi@yahoo.it','+390987654321','+393209876543','2023-03-20',1,1800,1,'2025-09-25 14:37:46');
INSERT INTO "employees" VALUES (3,'EMP003','Luca','Verdi','luca.verdi@dbsmartapi.com','luca.verdi@libero.it','+390555123456','+393401234567','2023-06-10',2,2000,1,'2025-09-25 14:37:46');
INSERT INTO "employees" VALUES (4,'EMP004','Anna','Neri','anna.neri@dbsmartapi.com','anna.neri@outlook.com','+390666234567','+393562345678','2023-09-01',1,1900,1,'2025-09-25 14:37:46');
INSERT INTO "employees" VALUES (5,'EMP005','Francesco','Blu','francesco.blu@dbsmartapi.com','francesco.blu@tiscali.it','+390777345678','+393673456789','2024-01-10',3,2800,1,'2025-09-25 14:37:46');
INSERT INTO "financial_categories" VALUES (1,'RENT','Affitti e Locazioni','cost','fixed','monthly','Affitto locali commerciali e magazzini','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (2,'UTIL','Utenze','cost','variable','monthly','Energia elettrica, gas, acqua, telefono','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (3,'SALARY','Stipendi e Salari','cost','fixed','monthly','Retribuzioni dipendenti e contributi','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (4,'SUPPLIES','Forniture Ufficio','cost','variable',NULL,'Materiali per ufficio e cancelleria','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (5,'MKTG','Marketing e Pubblicità','cost','variable',NULL,'Promozioni, advertising, materiale promozionale','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (6,'MAINT','Manutenzioni','cost','variable',NULL,'Riparazioni e manutenzioni attrezzature','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (7,'INSUR','Assicurazioni','cost','fixed','yearly','Polizze assicurative aziendali','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (8,'TAX','Tasse e Imposte','cost','variable','quarterly','IVA, imposte dirette e indirette','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (9,'FOOD','Acquisti Prodotti Alimentari','cost','variable',NULL,'Materie prime e prodotti finiti alimentari','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (10,'CLEAN','Prodotti Pulizia','cost','variable',NULL,'Detergenti e materiali per pulizia','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (11,'FOOD_SALES','Vendite Prodotti Alimentari','revenue','primary',NULL,'Ricavi da vendita prodotti panetteria','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (12,'BAKE_SALES','Vendite Prodotti da Forno','revenue','primary',NULL,'Ricavi da vendita pane e dolci','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (13,'BEVERAGE','Vendite Bevande','revenue','primary',NULL,'Ricavi da vendita bevande e caffetteria','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (14,'CATERING','Servizi Catering','revenue','service',NULL,'Ricavi da servizi catering e eventi','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (15,'DELIVERY','Servizi Consegna','revenue','service',NULL,'Ricavi da servizi di consegna a domicilio','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (16,'OTHER_REV','Altri Ricavi','revenue','other',NULL,'Ricavi diversi e straordinari','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (17,'BANK_FEES','Commissioni Bancarie','both','service',NULL,'Commissioni su transazioni e servizi bancari','2025-09-25 14:38:17');
INSERT INTO "financial_categories" VALUES (18,'CONSULTING','Consulenze','both','service',NULL,'Spese e ricavi per consulenze professionali','2025-09-25 14:38:17');
INSERT INTO "keycloak_sessions" VALUES (1,1,'kc-session-f47ac10b-58cc-4372','a1b2c3d4e5f67890123456789012345678901234567890123456789012345678','2025-09-25 15:37:29','192.168.1.100','2025-09-25 14:37:29');
INSERT INTO "keycloak_sessions" VALUES (2,2,'kc-session-6ba7b810-9dad-11d1','b2c3d4e5f67890123456789012345678901234567890123456789012345679','2025-09-25 15:37:29','192.168.1.101','2025-09-25 14:37:29');
INSERT INTO "keycloak_sessions" VALUES (3,3,'kc-session-6ba7b811-9dad-11d1','c3d4e5f67890123456789012345678901234567890123456789012345680','2025-09-25 15:37:29','192.168.1.102','2025-09-25 14:37:29');
INSERT INTO "keycloak_sessions" VALUES (4,4,'kc-session-6ba7b812-9dad-11d1','d4e5f67890123456789012345678901234567890123456789012345681','2025-09-25 15:37:29','192.168.1.103','2025-09-25 14:37:29');
INSERT INTO "locations" VALUES (1,'STORE01','Main Store','store','Via Roma 123','Milan','20100','ITA',NULL,'+390212345678','store01@dbsmartapi.com','08:00:00','20:00:00',1,'','2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "locations" VALUES (2,'WAREHOUSE01','Central Warehouse','warehouse','Via Industria 456','Milan','20100','ITA',NULL,'+390212345679','warehouse01@dbsmartapi.com','06:00:00','18:00:00',1,'','2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "locations" VALUES (3,'OFFICE01','Administrative Office','office','Via Uffici 789','Milan','20100','ITA',NULL,'+390212345680','office01@dbsmartapi.com','09:00:00','17:00:00',1,'','2025-09-25 14:37:46','2025-09-25 14:37:46');
INSERT INTO "loyalty_cards" VALUES (1,1,'LC001234567890','active',125,225,100,NULL,'bronze','2024-01-10','2026-01-10','2024-09-15',8,145.5,1,'2024-01-10','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (2,2,'LC001234567891','active',285,385,100,NULL,'silver','2024-01-12','2026-01-12','2024-09-18',12,285.75,1,'2024-01-12','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (3,3,'LC001234567892','active',520,720,200,NULL,'gold','2024-01-05','2026-01-05','2024-09-19',15,520.3,1,'2024-01-05','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (4,4,'LC001234567893','active',45,89,44,NULL,'bronze','2024-01-15','2026-01-15','2024-09-10',5,89.25,1,'2024-01-15','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (5,5,'LC001234567894','active',1250,1500,250,NULL,'platinum','2024-02-01','2026-02-01','2024-09-17',20,1250.8,1,'2024-02-01','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (6,6,'LC001234567895','active',198,298,100,NULL,'silver','2024-02-10','2026-02-10','2024-09-16',9,198.4,1,'2024-02-10','2025-09-25 14:37:58');
INSERT INTO "loyalty_cards" VALUES (7,7,'LC001234567896','inactive',67,67,0,NULL,'bronze','2024-03-01','2026-03-01','2024-08-20',3,67.15,0,'2024-03-01','2025-09-25 14:37:58');
INSERT INTO "products" VALUES (1,'0111716','0132354','PANINO FARCITO','Panino farcito tradizionale','120g',1,1,6,'8011117160',NULL,'pcs','PANE','FARCITO','BARCODE',NULL,25,2.5,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (2,'0116453','0132355','TARALLI AL FINOCCHIO S.& D. GR.400','Taralli al finocchio tradizionali pugliesi','400g',1,1,6,'8011645300',NULL,'pcs','TARALLI','FINOCCHIO','BARCODE',NULL,22,3.2,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (3,'0116454','0132356','TARALLI PEPERONCINO S.& D. GR.400','Taralli piccanti al peperoncino','400g',1,1,6,'8011645400',NULL,'pcs','TARALLI','PEPERONCINO','BARCODE',NULL,22,3.2,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (4,'0116455','0132357','TARALLI OLIO OLIVA S.& D. GR.400','Taralli con olio extravergine di oliva','400g',1,1,6,'8011645500',NULL,'pcs','TARALLI','OLIO OLIVA','BARCODE',NULL,24,3.5,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (5,'0120359','0132358','BAGUETTE Gr240','Baguette francese croccante','240g',1,1,6,'8012035900',NULL,'pcs','PANE','BAGUETTE','BARCODE',NULL,30,1.8,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (6,'0120533','0132359','PANE CASARECCIO/AFFETT.PANIF.GIGLIO','Pane casareccio affettato artigianale','500g',1,1,6,'8012053300',NULL,'pcs','PANE','CASARECCIO','BARCODE',NULL,28,2.2,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (7,'0120535','0132360','PANE AFFET. INTEGR/CUSCINE."GIGLIO"','Pane integrale affettata a cuscini','500g',1,1,6,'8012053500',NULL,'pcs','PANE','INTEGRALE','BARCODE',NULL,29,2.4,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (8,'0120536','0132361','PANE CIABATTA/FILONCINI PAN.GIGLIO','Pane ciabatta e filoncini freschi','400g',1,1,6,'8012053600',NULL,'pcs','PANE','CIABATTA','BARCODE',NULL,26,1.9,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (9,'0120538','0132362','PANINI ROSETTE "PANIF.GIGLIO"','Panini rosette tradizionali','80g',1,1,6,'8012053800',NULL,'pcs','PANE','ROSETTE','BARCODE',NULL,32,0.6,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (10,'0120539','0132363','SANDWICHES "PANIF.GIGLIO"','Pane per sandwiches morbido','100g',1,1,6,'8012053900',NULL,'pcs','PANE','SANDWICHES','BARCODE',NULL,35,0.8,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (11,'0120546','0132364','FOCACCE "PANIF.GIGLIO"','Focacce artigianali condite','300g',1,1,6,'8012054600',NULL,'pcs','FOCACCIA','CONDITA','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (12,'0120547','0132365','PIZZETTE/PANE ARABO "PANIF.GIGLIO"','Pizzette e pane arabo misto','150g',1,1,6,'8012054700',NULL,'pcs','PANE','ARABO','BARCODE',NULL,31,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (13,'0120756','0132366','PAN DI SPAGNA "GIGLIO"','Pan di Spagna per dolci','300g',1,1,6,'8012075600',NULL,'pcs','DOLCI','PAN DI SPAGNA','BARCODE',NULL,40,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (14,'0120788','0132367','CASTAGNOLE FORNO RHUM 200G','Castagnole al forno con aroma rhum','200g',1,1,6,'8012078800',NULL,'pcs','DOLCI','CASTAGNOLE','BARCODE',NULL,45,0,'Contiene glutine, uova, alcol',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (15,'0120960','0132368','FILONCINO/CIABATTE SFUSI "GIGLIO"','Filoncino e ciabatte sfusi freschi','300g',1,1,6,'8012096000',NULL,'pcs','PANE','FILONCINO','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (16,'0121000','0132369','PANE DI SEMOLA AFFETTAT G500 FORTE','Pane di semola affettato premium','500g',1,1,6,'8012100000',NULL,'pcs','PANE','SEMOLA','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (17,'0121151','0132370','CANNOLI SIC.NOC&CAC.KG 1.5 SAP.VERI','Cannoli siciliani nocciola e cacao','1.5kg',1,1,6,'8012115100',NULL,'pcs','DOLCI','CANNOLI','BARCODE',NULL,50,0,'Contiene glutine, latte, frutta a guscio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (18,'0121319','0132371','PANE BASSO KG.1 SFUSO "FORTE"','Pane basso sfuso da forno','1kg',1,1,6,'8012131900',NULL,'pcs','PANE','BASSO','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (19,'0121321','0132372','FILONE SFUSO KG.3  FORTE','Filone grande sfuso da forno','3kg',1,1,6,'8012132100',NULL,'pcs','PANE','FILONE','BARCODE',NULL,23,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (20,'0121391','0132373','PAGNOTTINA SEMI GIRASOLE 70G HAUBIS','Pagnottina con semi di girasole','70g',1,1,6,'8012139100',NULL,'pcs','PANE','SEMI GIRASOLE','BARCODE',NULL,38,0,'Contiene glutine, semi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (21,'0121392','0132374','PANINO SPITZ AI CEREALI 90G HAUBIS','Panino spitz multicereali','90g',1,1,6,'8012139200',NULL,'pcs','PANE','CEREALI','BARCODE',NULL,36,0,'Contiene glutine, cereali',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (22,'0121396','0132375','BREZEN 100G HAUBIS','Brezen bavarese tradizionale','100g',1,1,6,'8012139600',NULL,'pcs','PANE','BREZEN','BARCODE',NULL,39,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (23,'0121695','0132376','PAN BARCHETTE BIANCHE G.400 PAC','Pan barchette bianche confezionate','400g',1,1,6,'8012169500',NULL,'pcs','PANE','BARCHETTE','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (24,'0121696','0132377','PAN BARCHETTE INTEGR. G.400 PAC','Pan barchette integrali confezionate','400g',1,1,6,'8012169600',NULL,'pcs','PANE','BARCHETTE INTEGRALI','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (25,'0121700','0132378','PANEA STIRATINI G.250 OLIVE NERE','Stiratini conditi olive nere','250g',1,1,6,'8012170000',NULL,'pcs','PANE','OLIVE NERE','BARCODE',NULL,34,0,'Contiene glutine, olive',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (26,'0121701','0132379','PANEA STIRATINI G.250 SESAMO PAC','Stiratini al sesamo confezionati','250g',1,1,6,'8012170100',NULL,'pcs','PANE','SESAMO','BARCODE',NULL,33,0,'Contiene glutine, sesamo',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (27,'0121758','0132380','FRISELLE GRANO DURO GR.350 "FORTE"','Friselle di grano duro pugliesi','350g',1,1,6,'8012175800',NULL,'pcs','FRISELLE','GRANO DURO','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (28,'0121759','0132381','FRISELLE INTEGRALI GR.350 "FORTE"','Friselle integrali tradizionali','350g',1,1,6,'8012175900',NULL,'pcs','FRISELLE','INTEGRALI','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (29,'0121788','0132382','TARALLI CLASSICI GR300"TESORI D`APU','Taralli classici pugliesi','300g',1,1,6,'8012178800',NULL,'pcs','TARALLI','CLASSICI','BARCODE',NULL,24,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (30,'0121789','0132383','TARALLI SEMI-FIN.GR300"TESORI D`APU','Taralli semi fini pugliesi','300g',1,1,6,'8012178900',NULL,'pcs','TARALLI','SEMI FINI','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (31,'0121790','0132384','TARALLI PIZZA GR300"TESORI D`APU','Taralli gusto pizza','300g',1,1,6,'8012179000',NULL,'pcs','TARALLI','PIZZA','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (32,'0121791','0132385','TARALLI CIPOLLA GR300"TESORI D`APU','Taralli alla cipolla','300g',1,1,6,'8012179100',NULL,'pcs','TARALLI','CIPOLLA','BARCODE',NULL,24,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (33,'0121792','0132386','TARALLI PEPERONC.GR300"TESORI D`APU','Taralli piccanti al peperoncino','300g',1,1,6,'8012179200',NULL,'pcs','TARALLI','PEPERONCINO','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (34,'0121793','0132387','TARALLI SESAMO GR300"TESORI D`APU','Taralli al sesamo croccanti','300g',1,1,6,'8012179300',NULL,'pcs','TARALLI','SESAMO','BARCODE',NULL,26,0,'Contiene glutine, sesamo',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (35,'0122062','0132388','PANEA GRISSINO SENZA SALE GR250 PAC','Grissini senza sale confezionati','250g',1,1,6,'8012206200',NULL,'pcs','GRISSINI','SENZA SALE','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (36,'0122063','0132389','PAN FRESELLA BIANCA GR.400 "PAC"','Pan fresella bianca tradizionale','400g',1,1,6,'8012206300',NULL,'pcs','FRISELLE','BIANCA','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (37,'0122066','0132390','TARALLI ASS.TI GR350(PZ20XCT) FORTE','Taralli assortiti multipack','350g',1,1,6,'8012206600',NULL,'pcs','TARALLI','ASSORTITI','BARCODE',NULL,23,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (38,'0122067','0132391','TARALLI OLIO MULTIPAC (8PZXCT)FORTE','Taralli olio multipack convenienza','400g',1,1,6,'8012206700',NULL,'pcs','TARALLI','OLIO','BARCODE',NULL,22,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (39,'0122123','0132392','PAN.FRESELLA INTEGR.GR.400 "PAC"','Pan fresella integrale salutare','400g',1,1,6,'8012212300',NULL,'pcs','FRISELLE','INTEGRALE','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (40,'0122125','0132393','FERRATELLE MORBIDE GR180 LE DELIZIE','Ferratelle morbide abruzzesi','180g',1,1,6,'8012212500',NULL,'pcs','DOLCI','FERRATELLE','BARCODE',NULL,42,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (41,'0122126','0132394','FERRATELLE FRIABILI GR180 LE DELIZI','Ferratelle friabili tradizionali','180g',1,1,6,'8012212600',NULL,'pcs','DOLCI','FERRATELLE','BARCODE',NULL,41,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (42,'0122127','0132395','PANE DI SEGALE DORALDO GR500"PAC','Pane di segale integrale','500g',1,1,6,'8012212700',NULL,'pcs','PANE','SEGALE','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (43,'0122128','0132396','PAGNOTTA "PANIFICIO LINDA"','Pagnotta artigianale Linda','600g',1,1,6,'8012212800',NULL,'pcs','PANE','PAGNOTTA','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (44,'0122129','0132397','PANE PIZZA "PANIFICIO LINDA"','Pane per pizza base sottile','400g',1,1,6,'8012212900',NULL,'pcs','PANE','PIZZA','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (45,'0122130','0132398','CUSCINETTO AFFETTATO "PANIF.LINDA"','Pane cuscinetto affettato','500g',1,1,6,'8012213000',NULL,'pcs','PANE','CUSCINETTO','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (46,'0122542','0132399','PANE TIPO CONTADINO "PANIF.LINDA"','Pane tipo contadino rustico','700g',1,1,6,'8012254200',NULL,'pcs','PANE','CONTADINO','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (47,'0122131','0132400','PANE ARABO "PANIFICIO LINDA"','Pane arabo tradizionale','200g',1,1,6,'8012213100',NULL,'pcs','PANE','ARABO','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (48,'0122132','0132401','PAGNOTTA  CONF.KG1"OROPAN"','Pagnotta confezionata Oropan','1kg',1,1,6,'8012213200',NULL,'pcs','PANE','PAGNOTTA','BARCODE',NULL,24,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (49,'0122133','0132402','PANE BASSO AFF.GR.500 FORTE','Pane basso affettato Forte','500g',1,1,6,'8012213300',NULL,'pcs','PANE','BASSO','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (50,'0199999','0132403','REPARTO PANE E PASTICERIA','Articolo generico reparto pane','1kg',1,1,6,'8019999900',NULL,'pcs','GENERICO','REPARTO','MANUAL',NULL,20,0,'Vari allergeni',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (51,'0123840','0132404','CASARECCIO CONF. KG.1.6 "ALBERTO IL','Pane casareccio Alberto Il Fornaio','1.6kg',1,1,6,'8012384000',NULL,'pcs','PANE','CASARECCIO','BARCODE',NULL,23,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (52,'0123841','0132405','PANE ARABO CONF.KG.0.16 "ALBERTO IL','Pane arabo Alberto Il Fornaio','160g',1,1,6,'8012384100',NULL,'pcs','PANE','ARABO','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (53,'0123842','0132406','FILETTA ALBERTO IL FORNAIO','Filetta tradizionale Alberto','400g',1,1,6,'8012384200',NULL,'pcs','PANE','FILETTA','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (54,'0123843','0132407','PANE CASARECCIO 1.6 KG ALBERTO IL F','Pane casareccio grande Alberto','1.6kg',1,1,6,'8012384300',NULL,'pcs','PANE','CASARECCIO','BARCODE',NULL,22,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (55,'0123844','0132408','PANE FRANCESE 250Gca ALBERTO IL FOR','Pane francese Alberto Il Fornaio','250g',1,1,6,'8012384400',NULL,'pcs','PANE','FRANCESE','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (56,'0123845','0132409','PANINI FRANCESI GR.0.70 "ALBERTO IL','Panini francesi piccoli Alberto','70g',1,1,6,'8012384500',NULL,'pcs','PANE','PANINI FRANCESI','BARCODE',NULL,38,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (57,'0123846','0132410','PANE ARABO GR.85 "ALBERTO IL FORNAI','Pane arabo singolo Alberto','85g',1,1,6,'8012384600',NULL,'pcs','PANE','ARABO','BARCODE',NULL,40,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (58,'0123847','0132411','CASARECCIO SCURO KG.1.6"ALBERTO IL','Pane casareccio scuro integrale','1.6kg',1,1,6,'8012384700',NULL,'pcs','PANE','CASARECCIO SCURO','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (59,'0123848','0132412','FILETTA CONF. A META` G.470 "ALBERT','Filetta confezionata a metà','470g',1,1,6,'8012384800',NULL,'pcs','PANE','FILETTA','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (60,'0123849','0132413','PANE COTTO LEGNA C/PATATE DONATELLI','Pane cotto a legna con patate','600g',1,1,6,'8012384900',NULL,'pcs','PANE','COTTO LEGNA','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (61,'0123850','0132414','PIZZA ALL`OLIO "DONATELLI"','Pizza bianca all olio Donatelli','300g',1,1,6,'8012385000',NULL,'pcs','PIZZA','OLIO','BARCODE',NULL,31,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (62,'0123851','0132415','PIZZA ROSSA "DONATELLI"','Pizza rossa con pomodoro','320g',1,1,6,'8012385100',NULL,'pcs','PIZZA','ROSSA','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (63,'0123852','0132416','PANINI ALL`OLIO DONATELLI','Panini conditi olio Donatelli','100g',1,1,6,'8012385200',NULL,'pcs','PANE','OLIO','BARCODE',NULL,34,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (64,'0123853','0132417','CASERECCIO DI MUSCIANO','Pane casareccio di Musciano','800g',1,1,6,'8012385300',NULL,'pcs','PANE','CASARECCIO','BARCODE',NULL,24,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (65,'0123854','0132418','SFILATINI DI MUSCIANO','Sfilatini artigianali Musciano','200g',1,1,6,'8012385400',NULL,'pcs','PANE','SFILATINI','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (66,'0123855','0132419','CIABATTA DI MUSCIANO','Ciabatta tradizionale Musciano','350g',1,1,6,'8012385500',NULL,'pcs','PANE','CIABATTA','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (67,'0123856','0132420','FOCACCIA DI MUSCIANO','Focaccia artigianale Musciano','400g',1,1,6,'8012385600',NULL,'pcs','FOCACCIA','ARTIGIANALE','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (68,'0123857','0132421','PANINI ALL OLIO','Panini conditi all olio','90g',1,1,6,'8012385700',NULL,'pcs','PANE','OLIO','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (69,'0123858','0132422','PANINI EMULSIO','Panini emulsionati speciali','100g',1,1,6,'8012385800',NULL,'pcs','PANE','EMULSIO','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (70,'0123859','0132423','PANE AFFETTATO DI MUSCIANO','Pane affettato artigianale','500g',1,1,6,'8012385900',NULL,'pcs','PANE','AFFETTATO','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (71,'0123860','0132424','PANE INTEGRALI DI MUSCIANO','Pane integrale Musciano','600g',1,1,6,'8012386000',NULL,'pcs','PANE','INTEGRALE','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (72,'0123861','0132425','BISCOTTI CASERECCI DI MUSCIANO','Biscotti caserecci tradizionali','300g',1,1,6,'8012386100',NULL,'pcs','DOLCI','BISCOTTI','BARCODE',NULL,38,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (73,'0123862','0132426','BISCOTTI CASERECCI','Biscotti caserecci generici','250g',1,1,6,'8012386200',NULL,'pcs','DOLCI','BISCOTTI','BARCODE',NULL,40,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (74,'0123863','0132427','MARITOZZI','Maritozzi romani tradizionali','120g',1,1,6,'8012386300',NULL,'pcs','DOLCI','MARITOZZI','BARCODE',NULL,36,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (75,'0123864','0132428','FIADONE GRANDE DI MUSCIANO','Fiadone grande abruzzese','800g',1,1,6,'8012386400',NULL,'pcs','DOLCI','FIADONE','BARCODE',NULL,42,0,'Contiene glutine, uova, formaggi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (76,'0121393','0132429','PANE DI SEGALE 700G HAUBIS','Pane di segale integrale Haubis','700g',1,1,6,'8012139300',NULL,'pcs','PANE','SEGALE','BARCODE',NULL,31,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (77,'0121394','0132430','PAGNOTTINA SEMI ZUCCA 60G HAUBIS','Pagnottina con semi di zucca','60g',1,1,6,'8012139400',NULL,'pcs','PANE','SEMI ZUCCA','BARCODE',NULL,42,0,'Contiene glutine, semi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (78,'0121395','0132431','PANE TRE CIME BIO 500G HAUBI','Pane biologico Tre Cime','500g',1,1,6,'8012139500',NULL,'pcs','PANE','BIO','BARCODE',NULL,35,0,'Contiene glutine, biologico',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (79,'0135618','0132432','BAGUETTE GR 270','Baguette tradizionale francese','270g',1,1,6,'8013561800',NULL,'pcs','PANE','BAGUETTE','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (80,'0135619','0132433','LINGUE CROCCANTI NATURALI GR.150','Lingue croccanti naturali','150g',1,1,6,'8013561900',NULL,'pcs','PANE','CROCCANTI','BARCODE',NULL,40,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (81,'0135620','0132434','LINGUE CROCCANTI ROSMARINO GR.150','Lingue croccanti al rosmarino','150g',1,1,6,'8013562000',NULL,'pcs','PANE','ROSMARINO','BARCODE',NULL,41,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (82,'0135621','0132435','GHIOTTINA AL NATURALE GR.150','Ghiottina naturale croccante','150g',1,1,6,'8013562100',NULL,'pcs','PANE','GHIOTTINA','BARCODE',NULL,38,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (83,'0135622','0132436','GHIOTTINA AL ROSMARINO GR.150','Ghiottina aromatizzata rosmarino','150g',1,1,6,'8013562200',NULL,'pcs','PANE','ROSMARINO','BARCODE',NULL,39,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (84,'0135623','0132437','TORTA TERAMANA','Torta dolce teramana tradizionale','600g',1,1,6,'8013562300',NULL,'pcs','DOLCI','TORTA','BARCODE',NULL,45,0,'Contiene glutine, uova, mandorle',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (85,'0161150','0132438','BASI PIZZA PRECOTTE BIANCA MENCHETT','Basi pizza precotte bianche','300g',1,1,6,'8016115000',NULL,'pcs','PIZZA','PRECOTTA','BARCODE',NULL,43,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (86,'0161151','0132439','BASI PIZZA PRECOTTE ROSSA MENCHETTI','Basi pizza precotte rosse','320g',1,1,6,'8016115100',NULL,'pcs','PIZZA','PRECOTTA ROSSA','BARCODE',NULL,44,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (87,'0189126','0132440','SOSPIRI CHANTILLY 70G','Sospiri ripieni crema chantilly','70g',1,1,6,'8018912600',NULL,'pcs','DOLCI','SOSPIRI','BARCODE',NULL,46,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (88,'0198777','0132441','PANINO AL LATTE 55G','Panino dolce al latte','55g',1,1,6,'8019877700',NULL,'pcs','DOLCI','PANINO LATTE','BARCODE',NULL,37,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (89,'0198778','0132442','MINI PANINI AL LATTE 24G','Mini panini al latte dolci','24g',1,1,6,'8019877800',NULL,'pcs','DOLCI','MINI PANINI','BARCODE',NULL,42,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (90,'0191206','0132443','DONUTS ZEBRATO CIOCCOLATO 68G','Donut zebrato al cioccolato','68g',1,1,6,'8019120600',NULL,'pcs','DOLCI','DONUT','BARCODE',NULL,36,0,'Contiene glutine, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (91,'0191210','0132444','OREO DONUT 73G','Donut gusto biscotti Oreo','73g',1,1,6,'8019121000',NULL,'pcs','DOLCI','DONUT OREO','BARCODE',NULL,38,0,'Contiene glutine, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (92,'0191256','0132445','MINI CLASSIC MIX DONUT 22G','Mini donut classici assortiti','22g',1,1,6,'8019125600',NULL,'pcs','DOLCI','MINI DONUT','BARCODE',NULL,42,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (93,'0191267','0132446','MILKA DONUT 56G','Donut al cioccolato Milka','56g',1,1,6,'8019126700',NULL,'pcs','DOLCI','DONUT MILKA','BARCODE',NULL,38,0,'Contiene glutine, cacao, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (94,'0191272','0132447','DONUT SIMPSON PINK 55G','Donut rosa dei Simpson','55g',1,1,6,'8019127200',NULL,'pcs','DOLCI','DONUT SIMPSON','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (95,'0220424','0132448','PANE ARABO CLASSICO 300G','Pane arabo tradizionale','300g',1,1,6,'8022042400',NULL,'pcs','PANE','ARABO','BARCODE',NULL,37,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (96,'0221521','0132449','FOCACCINA 5 MORSI OLIVE POM.180G','Focaccina olive e pomodori','180g',1,1,6,'8022152100',NULL,'pcs','FOCACCIA','OLIVE POMODORI','BARCODE',NULL,37,0,'Contiene glutine, olive',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (97,'0222988','0132450','PASTICCIOTTO AL CIOCCOLATO 105G','Pasticciotto leccese cioccolato','105g',1,1,6,'8022299800',NULL,'pcs','DOLCI','PASTICCIOTTO','BARCODE',NULL,38,0,'Contiene glutine, cacao, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (98,'0145789','0132451','CORNETTO SEMPLICE 80G','Cornetto vuoto classico','80g',1,1,6,'8014578900',NULL,'pcs','DOLCI','CORNETTO','BARCODE',NULL,35,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (99,'0145790','0132452','CORNETTO CREMA 90G','Cornetto ripieno crema','90g',1,1,6,'8014579000',NULL,'pcs','DOLCI','CORNETTO CREMA','BARCODE',NULL,38,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (100,'0190234','0132453','BOMBOLONE CREMA 100G','Bombolone ripieno crema','100g',1,1,6,'8019023400',NULL,'pcs','DOLCI','BOMBOLONE','BARCODE',NULL,40,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (101,'0190235','0132454','BOMBOLONE NUTELLA 100G','Bombolone ripieno Nutella','100g',1,1,6,'8019023500',NULL,'pcs','DOLCI','BOMBOLONE NUTELLA','BARCODE',NULL,42,0,'Contiene glutine, uova, nocciole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (102,'0156890','0132455','MARITOZZO CLASSICO 120G','Maritozzo romano tradizionale','120g',1,1,6,'8015689000',NULL,'pcs','DOLCI','MARITOZZO','BARCODE',NULL,33,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (103,'0156891','0132456','MARITOZZO PANNA 130G','Maritozzo con panna montata','130g',1,1,6,'8015689100',NULL,'pcs','DOLCI','MARITOZZO PANNA','BARCODE',NULL,36,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (104,'0178945','0132457','CROSTATA MARMELLATA 200G','Crostata marmellata albicocche','200g',1,1,6,'8017894500',NULL,'pcs','DOLCI','CROSTATA','BARCODE',NULL,30,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (105,'0178946','0132458','CROSTATA NUTELLA 220G','Crostata ripieno Nutella','220g',1,1,6,'8017894600',NULL,'pcs','DOLCI','CROSTATA NUTELLA','BARCODE',NULL,32,0,'Contiene glutine, uova, nocciole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (106,'0199567','0132459','GRISSINI TORINESI 250G','Grissini torinesi tradizionali','250g',1,1,6,'8019956700',NULL,'pcs','PANE','GRISSINI','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (107,'0199568','0132460','TARALLI PUGLIESI 300G','Taralli pugliesi classici','300g',1,1,6,'8019956800',NULL,'pcs','TARALLI','PUGLIESI','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (108,'0203456','0132461','PANE PUGLIESE 800G','Pane pugliese tradizionale','800g',1,1,6,'8020345600',NULL,'pcs','PANE','PUGLIESE','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (109,'0203457','0132462','PANE SICILIANO 600G','Pane siciliano con sesamo','600g',1,1,6,'8020345700',NULL,'pcs','PANE','SICILIANO','BARCODE',NULL,27,0,'Contiene glutine, sesamo',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (110,'0178923','0132463','SFOGLIATELLE RICCIA 80G','Sfogliatelle riccia napoletana','80g',1,1,6,'8017892300',NULL,'pcs','DOLCI','SFOGLIATELLE','BARCODE',NULL,45,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (111,'0230100','0132464','UCCELLETTI LE BRICIOLE','Uccelletti dolci Le Briciole','150g',1,1,6,'8023010000',NULL,'pcs','DOLCI','UCCELLETTI','BARCODE',NULL,40,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (112,'0230101','0132465','PLUMCAKE SENZA LATTOSIO MELOGRANO','Plumcake senza lattosio','300g',1,1,6,'8023010100',NULL,'pcs','DOLCI','PLUMCAKE','BARCODE',NULL,35,0,'Contiene glutine, senza lattosio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (113,'0230102','0132466','CIAMBELLONE LIMONE KG1.7 KAMI`','Ciambellone al limone grande','1.7kg',1,1,6,'8023010200',NULL,'pcs','DOLCI','CIAMBELLONE','BARCODE',NULL,28,0,'Contiene glutine, uova, limone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (114,'0230103','0132467','MINI RUSTICHELLA SEMOLA G.140 CONAD','Mini rustichella semola Conad','140g',1,1,6,'8023010300',NULL,'pcs','PANE','RUSTICHELLA','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (115,'0230104','0132468','BAGUETTE GR.240 CONAD','Baguette Conad da 240g','240g',1,1,6,'8023010400',NULL,'pcs','PANE','BAGUETTE','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (116,'0230105','0132469','BAGUETTE AI SEMI G.280 CONAD','Baguette ai semi Conad','280g',1,1,6,'8023010500',NULL,'pcs','PANE','BAGUETTE SEMI','BARCODE',NULL,32,0,'Contiene glutine, semi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (117,'0230106','0132470','PAGNOTTA INT. AL FARRO G.400 CONAD','Pagnotta integrale al farro','400g',1,1,6,'8023010600',NULL,'pcs','PANE','FARRO','BARCODE',NULL,34,0,'Contiene glutine, farro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (118,'0230107','0132471','PANETTO PUGLIESE 400 G','Panetto pugliese tradizionale','400g',1,1,6,'8023010700',NULL,'pcs','PANE','PANETTO','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (119,'0121397','0132472','BREZEN BRIOCHE 85G HAUBIS','Brezen brioche Haubis','85g',1,1,6,'8012139700',NULL,'pcs','DOLCI','BREZEN BRIOCHE','BARCODE',NULL,40,0,'Contiene glutine, uova, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (120,'0121398','0132473','PANINO PROTEICO 82G HAUBIS','Panino proteico Haubis','82g',1,1,6,'8012139800',NULL,'pcs','PANE','PROTEICO','BARCODE',NULL,38,0,'Contiene glutine, proteine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (121,'0230108','0132474','CASARECCIO PUGLIESE 400 g','Pane casareccio pugliese','400g',1,1,6,'8023010800',NULL,'pcs','PANE','CASARECCIO','BARCODE',NULL,25,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (122,'0230109','0132475','TIRAMISU` MONOPORZIONE 120G','Tiramisù monoporzione','120g',1,1,6,'8023010900',NULL,'pcs','DOLCI','TIRAMISU','BARCODE',NULL,48,0,'Contiene glutine, uova, caffè, mascarpone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (123,'0230110','0132476','FERRATELLE 200G','Ferratelle abruzzesi tradizionali','200g',1,1,6,'8023011000',NULL,'pcs','DOLCI','FERRATELLE','BARCODE',NULL,38,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (124,'0230111','0132477','CORNETTO MULTIC.SALATO 85G(40PZXCT)','Cornetto multicereali salato','85g',1,1,6,'8023011100',NULL,'pcs','SALATI','CORNETTO','BARCODE',NULL,36,0,'Contiene glutine, cereali',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (125,'0230112','0132478','GRISSONE SFOGLIATO 117G','Grissone sfogliato grande','117g',1,1,6,'8023011200',NULL,'pcs','PANE','GRISSONE','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (126,'0230113','0132479','STRUDEL GRECO SPIN/FETA 125G(PZ50XC','Strudel greco spinaci e feta','125g',1,5,6,'8023011300',NULL,'pcs','SALATI','STRUDEL','BARCODE',NULL,42,0,'Contiene glutine, formaggio, spinaci',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (127,'0230114','0132480','ARAGOSTINE LIMONE 1.5KG','Aragostine al limone grandi','1.5kg',1,1,6,'8023011400',NULL,'pcs','DOLCI','ARAGOSTINE','BARCODE',NULL,35,0,'Contiene glutine, limone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (128,'0230115','0132481','SFOGLIAT.RICCIA GRANDE130G(45PZXCT)','Sfogliatella riccia grande','130g',1,5,6,'8023011500',NULL,'pcs','DOLCI','SFOGLIATELLA','BARCODE',NULL,46,0,'Contiene glutine, uova, ricotta',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (129,'0230116','0132482','GIRELLA AI FORMAGGI 126G','Girella salata ai formaggi','126g',1,1,6,'8023011600',NULL,'pcs','SALATI','GIRELLA','BARCODE',NULL,38,0,'Contiene glutine, formaggi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (130,'0230117','0132483','CALZONE FORNO MARGH.120G(40PZXCT)','Calzone al forno margherita','120g',1,1,6,'8023011700',NULL,'pcs','SALATI','CALZONE','BARCODE',NULL,40,0,'Contiene glutine, pomodoro, mozzarella',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (131,'0230118','0132484','DANESINA NOCI PECAN 98G (48PZ)','Danesina con noci pecan','98g',1,1,6,'8023011800',NULL,'pcs','DOLCI','DANESINA','BARCODE',NULL,44,0,'Contiene glutine, uova, noci pecan',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (132,'0230119','0132485','RUSTICI MIGNON 6 GUSTI(6KGXCT)','Rustici mignon assortiti','150g',1,1,6,'8023011900',NULL,'pcs','SALATI','RUSTICI','BARCODE',NULL,36,0,'Contiene glutine, vari ingredienti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (133,'0230120','0132486','DONUT LAMPONE CHEESECAKE 69G','Donut lampone e cheesecake','69g',1,7,6,'8023012000',NULL,'pcs','DOLCI','DONUT','BARCODE',NULL,42,0,'Contiene glutine, lamponi, formaggio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (134,'0230121','0132487','PIZZETTE SFOGLIA MIGNON 25G(5KG)','Pizzette sfoglia mignon','25g',1,1,6,'8023012100',NULL,'pcs','SALATI','PIZZETTE','BARCODE',NULL,38,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (135,'0230122','0132488','DOLCEMELE MELINDA 90G','Dolce di mele Melinda','90g',1,1,6,'8023012200',NULL,'pcs','DOLCI','DOLCEMELE','BARCODE',NULL,40,0,'Contiene glutine, mele',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (136,'0230123','0132489','PANCAKE 40G (40PZXCT)','Pancake americani','40g',1,1,6,'8023012300',NULL,'pcs','DOLCI','PANCAKE','BARCODE',NULL,38,0,'Contiene glutine, uova, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (137,'0230124','0132490','CIAMBELLA ZUCCHERATA 70G (40PZXCT)','Ciambella zuccherata dolce','70g',1,1,6,'8023012400',NULL,'pcs','DOLCI','CIAMBELLA','BARCODE',NULL,36,0,'Contiene glutine, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (138,'0230125','0132491','WAFFLE 115G','Waffle belga tradizionale','115g',1,1,6,'8023012500',NULL,'pcs','DOLCI','WAFFLE','BARCODE',NULL,40,0,'Contiene glutine, uova, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (139,'0230126','0132492','CORNETTINO WURSTEL (6KGXCT)','Cornettino salato wurstel','80g',1,1,6,'8023012600',NULL,'pcs','SALATI','CORNETTINO','BARCODE',NULL,34,0,'Contiene glutine, wurstel',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (140,'0230127','0132493','FIADONI 5KG','Fiadoni abruzzesi tradizionali','100g',1,8,6,'8023012700',NULL,'pcs','DOLCI','FIADONI','BARCODE',NULL,42,0,'Contiene glutine, uova, formaggio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (141,'0230128','0132494','FOCACCINA TRADIZIONALE 80G(65PZXCT)','Focaccina tradizionale','80g',1,1,6,'8023012800',NULL,'pcs','PANE','FOCACCINA','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (142,'0230129','0132495','PINK DONUT 55G','Donut rosa decorato','55g',1,1,6,'8023012900',NULL,'pcs','DOLCI','DONUT ROSA','BARCODE',NULL,35,0,'Contiene glutine, coloranti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (143,'0230130','0132496','CORNETTO ALLA CURCUMA 80G','Cornetto speziato curcuma','80g',1,1,6,'8023013000',NULL,'pcs','DOLCI','CORNETTO CURCUMA','BARCODE',NULL,37,0,'Contiene glutine, curcuma',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (144,'0230131','0132497','MELIZIA MELA CUB.95G (60PZXCT)','Melizia mela cubetti','95g',1,1,6,'8023013100',NULL,'pcs','DOLCI','MELIZIA','BARCODE',NULL,39,0,'Contiene glutine, mele',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (145,'0230132','0132498','FOCACCIA TRADIZ.PREMIUM 600G(10PZ)','Focaccia tradizionale premium','600g',1,1,6,'8023013200',NULL,'pcs','PANE','FOCACCIA PREMIUM','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (146,'0230133','0132499','PIZZETTE PANE','Pizzette di pane semplici','50g',1,1,6,'8023013300',NULL,'pcs','SALATI','PIZZETTE','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (147,'0230134','0132500','HOT DOG','Hot dog completo','150g',1,1,6,'8023013400',NULL,'pcs','SALATI','HOT DOG','BARCODE',NULL,35,0,'Contiene glutine, wurstel',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (148,'0230135','0132501','KRAPFEN CREMA 70G (48PZXCT)','Krapfen ripieno di crema','70g',1,1,6,'8023013500',NULL,'pcs','DOLCI','KRAPFEN','BARCODE',NULL,38,0,'Contiene glutine, uova, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (149,'0230136','0132502','CROISSANT BEUMIER 70G','Croissant francese Beumier','70g',1,1,6,'8023013600',NULL,'pcs','DOLCI','CROISSANT','BARCODE',NULL,40,0,'Contiene glutine, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (150,'0230137','0132503','ZEPPOLE FORNO GRANDI CREMA 120Gx12','Zeppole al forno con crema','120g',1,1,6,'8023013700',NULL,'pcs','DOLCI','ZEPPOLE','BARCODE',NULL,42,0,'Contiene glutine, uova, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (151,'0230138','0132504','PINSA CLASSICA 230G AMBIENT PINSAMI','Pinsa romana classica','230g',1,1,6,'8023013800',NULL,'pcs','SALATI','PINSA','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (152,'0230139','0132505','PIZZETTE PANE ZUCCHINE GR.30 KG.3','Pizzette pane con zucchine','30g',1,1,6,'8023013900',NULL,'pcs','SALATI','PIZZETTE ZUCCHINE','BARCODE',NULL,38,0,'Contiene glutine, zucchine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (153,'0230140','0132506','ZEPPOLE FORNO MIGNON CREMA 1.5KG','Zeppole mignon con crema','50g',1,1,6,'8023014000',NULL,'pcs','DOLCI','ZEPPOLE MIGNON','BARCODE',NULL,40,0,'Contiene glutine, uova, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (154,'0230141','0132507','PANE BASSO INTEGR. SEMI DI GIRASOLE','Pane basso integrale semi','400g',1,1,6,'8023014100',NULL,'pcs','PANE','INTEGRALE SEMI','BARCODE',NULL,32,0,'Contiene glutine, semi girasole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (155,'0230142','0132508','CIABATTA DI GRANO DURO INTEGRALE','Ciabatta grano duro integrale','350g',1,1,6,'8023014200',NULL,'pcs','PANE','CIABATTA INTEGRALE','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (156,'0230143','0132509','FRESELLA BIANCA 200G PAN','Fresella bianca tradizionale','200g',1,1,6,'8023014300',NULL,'pcs','PANE','FRESELLA','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (157,'0230144','0132510','FRESELLA INTEGRALE 200G PAN','Fresella integrale salutare','200g',1,1,6,'8023014400',NULL,'pcs','PANE','FRESELLA INTEGRALE','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (158,'0230145','0132511','CIAMBELLONE CACAO 1.7KG KAMI`','Ciambellone al cacao grande','1.7kg',1,1,6,'8023014500',NULL,'pcs','DOLCI','CIAMBELLONE CACAO','BARCODE',NULL,28,0,'Contiene glutine, cacao, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (159,'0230146','0132512','PINSA ROMANA 230G AMBIENT DI MARCO','Pinsa romana di Marco','230g',1,1,6,'8023014600',NULL,'pcs','SALATI','PINSA ROMANA','BARCODE',NULL,36,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (160,'0230147','0132513','PANE AI MIRTILLI 6.3KG','Pane dolce ai mirtilli','300g',1,1,6,'8023014700',NULL,'pcs','PANE','MIRTILLI','BARCODE',NULL,35,0,'Contiene glutine, mirtilli',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (161,'0230148','0132514','PANE PROTEIN 30 100G','Pane proteico 30% proteine','100g',1,1,6,'8023014800',NULL,'pcs','PANE','PROTEICO','BARCODE',NULL,40,0,'Contiene glutine, proteine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (162,'0230149','0132515','FRISELLE PUGLIESI 350 G SAPORI&DINT','Friselle pugliesi tradizionali','350g',1,1,6,'8023014900',NULL,'pcs','PANE','FRISELLE','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (163,'0230150','0132516','PANE AZZIMO 250 G GRAZIANO','Pane azzimo senza lievito','250g',1,1,6,'8023015000',NULL,'pcs','PANE','AZZIMO','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (164,'0230151','0132517','MINI CRESCIA 240G LA BOLLA','Mini crescia marchigiana','240g',1,1,6,'8023015100',NULL,'pcs','PANE','CRESCIA','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (165,'0230152','0132518','RUSTICA MIGNON AI FORMAGGI 80G','Rustica mignon formaggi','80g',1,1,6,'8023015200',NULL,'pcs','SALATI','RUSTICA','BARCODE',NULL,38,0,'Contiene glutine, formaggi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (166,'0230153','0132519','RUSTICA MIGNON SPINACI 80G','Rustica mignon spinaci','80g',1,1,6,'8023015300',NULL,'pcs','SALATI','RUSTICA SPINACI','BARCODE',NULL,37,0,'Contiene glutine, spinaci',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (167,'0230154','0132520','FOCACCIA BELLA PEPERONI FP','Focaccia bella ai peperoni','300g',1,1,6,'8023015400',NULL,'pcs','SALATI','FOCACCIA PEPERONI','BARCODE',NULL,35,0,'Contiene glutine, peperoni',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (168,'0230155','0132521','FOCACCIA BELLA POMODORO FP','Focaccia bella al pomodoro','300g',1,1,6,'8023015500',NULL,'pcs','SALATI','FOCACCIA POMODORO','BARCODE',NULL,34,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (169,'0230156','0132522','FOCACCIA RIP.PROSC./FORMAGGIO FP','Focaccia ripiena prosciutto','350g',1,2,6,'8023015600',NULL,'pcs','SALATI','FOCACCIA RIPIENA','BARCODE',NULL,38,0,'Contiene glutine, prosciutto, formaggio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (170,'0230157','0132523','MUFFIN NUTELLA T2 G.86X2','Muffin doppio alla Nutella','86g',1,1,6,'8023015700',NULL,'pcs','DOLCI','MUFFIN NUTELLA','BARCODE',NULL,42,0,'Contiene glutine, nocciole, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (171,'0230158','0132524','TARALLINI INTEGRALI CONAD GR.40X10','Tarallini integrali Conad','40g',1,1,6,'8023015800',NULL,'pcs','TARALLI','INTEGRALI','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (172,'0230159','0132525','SALTIMBOCCA CLASSICI 450G DE FENZA','Saltimbocca classici De Fenza','450g',1,1,6,'8023015900',NULL,'pcs','SALATI','SALTIMBOCCA','BARCODE',NULL,36,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (173,'0230160','0132526','BARRETTA CEREALI 140G','Barretta ai cereali energetica','140g',1,1,6,'8023016000',NULL,'pcs','DOLCI','BARRETTA','BARCODE',NULL,35,0,'Contiene glutine, cereali',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (174,'0230161','0132527','FOCACCIA ROMANA 400G','Focaccia romana tradizionale','400g',1,1,6,'8023016100',NULL,'pcs','SALATI','FOCACCIA ROMANA','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (175,'0230162','0132528','FOCACCIA RUSTICA 800G','Focaccia rustica grande','800g',1,1,6,'8023016200',NULL,'pcs','SALATI','FOCACCIA RUSTICA','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (176,'0230163','0132529','FOCACCIA TONDA OLIVE/POMO.750G(10PZ','Focaccia tonda olive pomodori','750g',1,1,6,'8023016300',NULL,'pcs','SALATI','FOCACCIA TONDA','BARCODE',NULL,33,0,'Contiene glutine, olive, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (177,'0230164','0132530','PAGNOTTA LIEV.NAT.MIELE/NOCI 500G','Pagnotta lievito naturale miele','500g',1,1,6,'8023016400',NULL,'pcs','PANE','PAGNOTTA MIELE','BARCODE',NULL,36,0,'Contiene glutine, miele, noci',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (178,'0230165','0132531','PANINO MULTIC.FARRO/FAR.PATATE 110G','Panino multicereali farro patate','110g',1,1,6,'8023016500',NULL,'pcs','PANE','PANINO MULTICEREALI','BARCODE',NULL,34,0,'Contiene glutine, farro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (179,'0230166','0132532','CRESCIA SFOGLIATA DI URBINO 450G','Crescia sfogliata marchigiana','450g',1,1,6,'8023016600',NULL,'pcs','PANE','CRESCIA SFOGLIATA','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (180,'0230167','0132533','TARALLI NAPOLET.EXTRA 250G DE FENZA','Taralli napoletani extra','250g',1,1,6,'8023016700',NULL,'pcs','TARALLI','NAPOLETANI','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (181,'0230168','0132534','TARALLI PROT.M/PACK 6X50G C.DEL GUS','Taralli proteici multipack','50g',1,1,6,'8023016800',NULL,'pcs','TARALLI','PROTEICI','BARCODE',NULL,30,0,'Contiene glutine, proteine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (182,'0230169','0132535','TARALLINI PUGLIESI 200G LA CASA DEL','Tarallini pugliesi Casa del Gusto','200g',1,1,6,'8023016900',NULL,'pcs','TARALLI','PUGLIESI','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (183,'0230170','0132536','PUCCIA ACQ.DI MARE 115GX2 C.DELGUST','Puccia acqua di mare doppia','115g',1,1,6,'8023017000',NULL,'pcs','PANE','PUCCIA','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (184,'0230171','0132537','CIAMBELLONE YOGURT 400G CASA DEL G.','Ciambellone allo yogurt','400g',1,1,6,'8023017100',NULL,'pcs','DOLCI','CIAMBELLONE YOGURT','BARCODE',NULL,33,0,'Contiene glutine, yogurt',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (185,'0230172','0132538','CIAMBELLONE VAR.CACAO 400G CASA D.G','Ciambellone variegato cacao','400g',1,1,6,'8023017200',NULL,'pcs','DOLCI','CIAMBELLONE CACAO','BARCODE',NULL,34,0,'Contiene glutine, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (186,'0230173','0132539','MIX PANINI COLORATI 26G','Mix panini colorati piccoli','26g',1,1,6,'8023017300',NULL,'pcs','PANE','PANINI COLORATI','BARCODE',NULL,38,0,'Contiene glutine, coloranti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (187,'0230174','0132540','FAGOTTINO GIANDUIA 104G','Fagottino ripieno gianduia','104g',1,1,6,'8023017400',NULL,'pcs','DOLCI','FAGOTTINO','BARCODE',NULL,44,0,'Contiene glutine, nocciole, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (188,'0230175','0132541','MARS DONUT 57G','Donut gusto Mars','57g',1,1,6,'8023017500',NULL,'pcs','DOLCI','DONUT MARS','BARCODE',NULL,39,0,'Contiene glutine, cacao, caramello',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (189,'0230176','0132542','MARITOZZO CON PANNA 90G','Maritozzo con panna fresca','90g',1,1,6,'8023017600',NULL,'pcs','DOLCI','MARITOZZO PANNA','BARCODE',NULL,36,0,'Contiene glutine, panna, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (190,'0230177','0132543','SBRODOLONI PISTACCHIO 100G','Sbrodoloni al pistacchio','100g',1,1,6,'8023017700',NULL,'pcs','DOLCI','SBRODOLONI','BARCODE',NULL,46,0,'Contiene glutine, pistacchi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (191,'0230178','0132544','SBRODOLONI ALLO ZABAIONE 100 G','Sbrodoloni allo zabaione','100g',1,1,6,'8023017800',NULL,'pcs','DOLCI','SBRODOLONI ZABAIONE','BARCODE',NULL,45,0,'Contiene glutine, uova, alcol',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (192,'0230179','0132545','MIGNON PISTACCHIO/LAMPONE 40G','Mignon pistacchio e lampone','40g',1,1,6,'8023017900',NULL,'pcs','DOLCI','MIGNON','BARCODE',NULL,48,0,'Contiene glutine, pistacchi, lamponi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (193,'0230180','0132546','PIZZA MARGHERITA 125 G','Pizza margherita classica','125g',1,1,6,'8023018000',NULL,'pcs','SALATI','PIZZA MARGHERITA','BARCODE',NULL,35,0,'Contiene glutine, pomodoro, mozzarella',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (194,'0230181','0132547','PIZZA PATATE E SALSICCIA 140 G','Pizza patate e salsiccia','140g',1,2,6,'8023018100',NULL,'pcs','SALATI','PIZZA SALSICCIA','BARCODE',NULL,37,0,'Contiene glutine, patate, salsiccia',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (195,'0207601','0132548','PANE FR.INTEGR.NOSTALGIA AFF.500G','Pane fresco integrale nostalgia','500g',1,1,6,'8020760100',NULL,'pcs','PANE','INTEGRALE NOSTALGIA','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (196,'0230182','0132549','PANE FRESCO CLASSICO TIPO 0 500G GR','Pane fresco classico tipo 0','500g',1,1,6,'8023018200',NULL,'pcs','PANE','FRESCO CLASSICO','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (197,'0230183','0132550','PAN BAULETTO SOFFICE 400G GR.IMPERO','Pan bauletto soffice','400g',1,1,6,'8023018300',NULL,'pcs','PANE','BAULETTO','BARCODE',NULL,28,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (198,'0230206','0132573','CIABATTINA FRESCA 130G GRAN.IMPERO','Ciabattina fresca Gran Impero','130g',1,1,6,'8023020600',NULL,'pcs','PANE','CIABATTINA','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (199,'0230207','0132574','PANE FR.DELIZIA 350G C/FRUTTA DISID','Pane delizia con frutta disidratata','350g',1,1,6,'8023020700',NULL,'pcs','PANE','DELIZIA FRUTTA','BARCODE',NULL,42,0,'Contiene glutine, frutta disidratata',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (200,'0230208','0132575','PANE FRESCO GRANO DURO 1KG GR.IMPER','Pane grano duro Gran Impero','1kg',1,1,6,'8023020800',NULL,'pcs','PANE','GRANO DURO','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (201,'0230209','0132576','PANE FRESCO GREZZO TIPO 2 800G GR.I','Pane grezzo tipo 2','800g',1,1,6,'8023020900',NULL,'pcs','PANE','GREZZO TIPO2','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (202,'0230210','0132577','PANE FR.INTEGR.NOSTALGIA AFF.500G','Pane integrale nostalgia affettato','500g',1,1,6,'8023021000',NULL,'pcs','PANE','INTEGRALE NOSTALGIA','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (203,'0230211','0132578','PANE FRESCO SCIAPO 750G GRAN.IMPERO','Pane sciapo Gran Impero','750g',1,1,6,'8023021100',NULL,'pcs','PANE','SCIAPO','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (204,'0230212','0132579','PANE DI SOLINA AGRIFORNO','Pane di solina Agriforno','400g',1,1,6,'8023021200',NULL,'pcs','PANE','SOLINA','BARCODE',NULL,45,0,'Contiene glutine, grano solina',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (205,'0230213','0132580','PANE GHIOTTO ALLA CURCUMA 109G','Pane ghiotto alla curcuma','109g',1,1,6,'8023021300',NULL,'pcs','PANE','CURCUMA','BARCODE',NULL,40,0,'Contiene glutine, curcuma',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (206,'0230214','0132581','PAPILLON 300G','Papillon dolce','300g',1,1,6,'8023021400',NULL,'pcs','DOLCI','PAPILLON','BARCODE',NULL,46,0,'Contiene glutine, burro, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (207,'0230215','0132582','CALZONE FRITTO PROSC/MOZZ.160G(30PZ','Calzone fritto prosciutto mozzarella','160g',1,2,6,'8023021500',NULL,'pcs','SALATI','CALZONE FRITTO','BARCODE',NULL,41,0,'Contiene glutine, prosciutto, mozzarella',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (208,'0230216','0132583','PANE AFFETTATO FERRETTI','Pane affettato Ferretti','500g',1,1,6,'8023021600',NULL,'pcs','PANE','AFFETTATO FERRETTI','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (209,'0230217','0132584','LA PINSA 250G MENCHETTI','La Pinsa Menchetti','250g',1,1,6,'8023021700',NULL,'pcs','SALATI','PINSA','BARCODE',NULL,39,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (210,'0230218','0132585','PANE SFUSO SAL/SENZA SAL.K.1 FORTI','Pane sfuso kg.1 salato/senza sale','1kg',1,1,6,'8023021800',NULL,'pcs','PANE','SFUSO KG1','BARCODE',NULL,24,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (211,'0230219','0132586','PANE SFUSO SAL/SENZA SAL.G500 FORTI','Pane sfuso 500g salato/senza sale','500g',1,1,6,'8023021900',NULL,'pcs','PANE','SFUSO 500G','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (212,'0230220','0132587','PANE SALATO/SENZA SALE G500 FORTI','Pane 500g salato/senza sale Forti','500g',1,1,6,'8023022000',NULL,'pcs','PANE','FORTI 500G','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (213,'0230221','0132588','PANE INTREGRALE/FRUSTE/CIABATTE/MAI','Pane integrale/fruste/ciabatte/mais','400g',1,1,6,'8023022100',NULL,'pcs','PANE','MISTO INTEGRALE','BARCODE',NULL,34,0,'Contiene glutine, mais',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (214,'0230222','0132589','PANINI ALL OLIO/SANDWICHES FORTI','Panini all olio/sandwiches Forti','300g',1,1,6,'8023022200',NULL,'pcs','PANE','PANINI OLIO','BARCODE',NULL,35,0,'Contiene glutine, olio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (215,'0230223','0132590','PANINI SOFFIATI FORTI','Panini soffiati Forti','200g',1,1,6,'8023022300',NULL,'pcs','PANE','SOFFIATI','BARCODE',NULL,38,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (216,'0230224','0132591','PANE RISO/SEGALE/CEREALI/KAMUT','Pane riso/segale/cereali/kamut','450g',1,1,6,'8023022400',NULL,'pcs','PANE','CEREALI MISTI','BARCODE',NULL,40,0,'Contiene glutine, riso, segale, kamut',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (217,'0230225','0132592','PIZZA AL POMODORO FORTI','Pizza al pomodoro Forti','150g',1,1,6,'8023022500',NULL,'pcs','SALATI','PIZZA POMODORO','BARCODE',NULL,36,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (218,'0230226','0132593','BISCOTTI FORTI','Biscotti artigianali Forti','250g',1,1,6,'8023022600',NULL,'pcs','DOLCI','BISCOTTI','BARCODE',NULL,42,0,'Contiene glutine, burro, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (219,'0230227','0132594','BOCCONOTTI/SFOGLIATE/UCCELL.FORTI','Bocconotti/sfogliate/uccelletti Forti','300g',1,1,6,'8023022700',NULL,'pcs','DOLCI','BOCCONOTTI MISTI','BARCODE',NULL,45,0,'Contiene glutine, marmellata, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (220,'0230228','0132595','MARITOZZI FORTI','Maritozzi Forti','200g',1,1,6,'8023022800',NULL,'pcs','DOLCI','MARITOZZI','BARCODE',NULL,40,0,'Contiene glutine, uvetta, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (221,'0230229','0132596','BAGUETTE GR.280 PANIF.VERDECCHIA','Baguette 280g Panificio Verdecchia','280g',1,1,6,'8023022900',NULL,'pcs','PANE','BAGUETTE','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (222,'0230230','0132597','FOCACCIA GR.300 PANIF.VERDECCHIA','Focaccia 300g Panificio Verdecchia','300g',1,1,6,'8023023000',NULL,'pcs','SALATI','FOCACCIA','BARCODE',NULL,37,0,'Contiene glutine, olio, rosmarino',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (223,'0230231','0132598','SANDWICHES PAN.VERDECCHIA','Sandwiches Panificio Verdecchia','200g',1,1,6,'8023023100',NULL,'pcs','PANE','SANDWICHES','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (224,'0230232','0132599','MARITOZZI CONF. PZ.3 VERDECCHIA','Maritozzi confezione 3 pezzi','300g',1,1,6,'8023023200',NULL,'pcs','DOLCI','MARITOZZI CONF','BARCODE',NULL,42,0,'Contiene glutine, uvetta, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (225,'0230233','0132600','PIZZA CROCCANTE VERDECCHIA','Pizza croccante Verdecchia','180g',1,1,6,'8023023300',NULL,'pcs','SALATI','PIZZA CROCCANTE','BARCODE',NULL,38,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (226,'0230234','0132601','PANINO PER HAMBURGER VERDECCHIA','Panino per hamburger Verdecchia','100g',1,1,6,'8023023400',NULL,'pcs','PANE','PANINO HAMBURGER','BARCODE',NULL,36,0,'Contiene glutine, sesamo',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (227,'0230235','0132602','PANE AI CEREALI PANIFICIO LINDA','Pane ai cereali Panificio Linda','400g',1,1,6,'8023023500',NULL,'pcs','PANE','CEREALI LINDA','BARCODE',NULL,39,0,'Contiene glutine, cereali misti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (228,'0230236','0132603','TARALLUCCI VINO TINTILLA G.250CIRU','Tarallucci vino Tintilla 250g','250g',1,1,6,'8023023600',NULL,'pcs','DOLCI','TARALLUCCI VINO','BARCODE',NULL,44,0,'Contiene glutine, vino tintilla',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (229,'0230237','0132604','CIAMBELLINE AL VINO G.250CIRUCCI','Ciambelline al vino 250g Cirucci','250g',1,1,6,'8023023700',NULL,'pcs','DOLCI','CIAMBELLINE VINO','BARCODE',NULL,43,0,'Contiene glutine, vino bianco',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (230,'0230238','0132605','MINI CORNETTI SFOGLIATI G.200CIRUC','Mini cornetti sfogliati 200g','200g',1,1,6,'8023023800',NULL,'pcs','DOLCI','MINI CORNETTI','BARCODE',NULL,46,0,'Contiene glutine, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (231,'0230239','0132606','CORNETTI SFOGLIATI G.180CIRUCCI','Cornetti sfogliati 180g Cirucci','180g',1,1,6,'8023023900',NULL,'pcs','DOLCI','CORNETTI SFOGLIATI','BARCODE',NULL,45,0,'Contiene glutine, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (232,'0230240','0132607','BISCOTTI DA LATTE G.350CIRUCCI','Biscotti da latte 350g Cirucci','350g',1,1,6,'8023024000',NULL,'pcs','DOLCI','BISCOTTI LATTE','BARCODE',NULL,41,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (233,'0230241','0132608','FERRATELLE MORBIDE G.150CIRUCCI','Ferratelle morbide 150g Cirucci','150g',1,1,6,'8023024100',NULL,'pcs','DOLCI','FERRATELLE MORBIDE','BARCODE',NULL,48,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (234,'0230242','0132609','FERRATELLE FRIABILI G.150CIRUCCI','Ferratelle friabili 150g Cirucci','150g',1,1,6,'8023024200',NULL,'pcs','DOLCI','FERRATELLE FRIABILI','BARCODE',NULL,47,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (235,'0230243','0132610','FAGOTTINI AMARENA/MAND.150G CIRUCCI','Fagottini amarena/mandorle 150g','150g',1,1,6,'8023024300',NULL,'pcs','DOLCI','FAGOTTINI AMARENA','BARCODE',NULL,50,0,'Contiene glutine, amarene, mandorle',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (236,'0230244','0132611','PANE GRATTUGGIATO TRIPLO PAN.LINDA','Pane grattugiato triplo Panificio Linda','500g',1,1,6,'8023024400',NULL,'pcs','PANE','GRATTUGIATO TRIPLO','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (237,'0230245','0132612','MOSTACCIOLI AMARENA/NOCCIOLA G.200','Mostaccioli amarena/nocciola 200g','200g',1,1,6,'8023024500',NULL,'pcs','DOLCI','MOSTACCIOLI','BARCODE',NULL,49,0,'Contiene glutine, amarene, nocciole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (238,'0230246','0132613','TOZZETTI ALLE MANDORLE G.200CIRUCC','Tozzetti alle mandorle 200g Cirucci','200g',1,1,6,'8023024600',NULL,'pcs','DOLCI','TOZZETTI MANDORLE','BARCODE',NULL,46,0,'Contiene glutine, mandorle',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (239,'0230247','0132614','PANE CASARECCIO BALDINI','Pane casareccio Baldini','500g',1,1,6,'8023024700',NULL,'pcs','PANE','CASARECCIO BALDINI','BARCODE',NULL,31,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (240,'0230248','0132615','PANINI GR.85 BALDINI','Panini 85g Baldini','85g',1,1,6,'8023024800',NULL,'pcs','PANE','PANINI BALDINI','BARCODE',NULL,37,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (241,'0230249','0132616','FOCACCIA BALDINI','Focaccia Baldini','250g',1,1,6,'8023024900',NULL,'pcs','SALATI','FOCACCIA BALDINI','BARCODE',NULL,35,0,'Contiene glutine, olio, erbe',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (242,'0230250','0132617','PANE GRATTUGIATO GR.500 BALDINI','Pane grattugiato 500g Baldini','500g',1,1,6,'8023025000',NULL,'pcs','PANE','GRATTUGIATO BALDINI','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (243,'0230251','0132618','GRISSIPIZZA CLASSICO BALDINI','Grissipizza classico Baldini','150g',1,1,6,'8023025100',NULL,'pcs','SALATI','GRISSIPIZZA','BARCODE',NULL,39,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (244,'0230252','0132619','PANE AFFETTATO BALDINI','Pane affettato Baldini','400g',1,1,6,'8023025200',NULL,'pcs','PANE','AFFETTATO BALDINI','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (245,'0230253','0132620','ROSETTE BALDINI','Rosette Baldini','300g',1,1,6,'8023025300',NULL,'pcs','PANE','ROSETTE','BARCODE',NULL,34,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (246,'0230254','0132621','PANINI SFUSI DE GIORGIS','Panini sfusi De Giorgis','250g',1,1,6,'8023025400',NULL,'pcs','PANE','PANINI SFUSI DG','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (247,'0230255','0132622','PANE G.250-500 SFUSO DE GIORGIS','Pane 250-500g sfuso De Giorgis','375g',1,1,6,'8023025500',NULL,'pcs','PANE','SFUSO MEDIO DG','BARCODE',NULL,29,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (248,'0230256','0132623','PANE G.501-1000 SFUSO DE GIORGIS','Pane 501-1000g sfuso De Giorgis','750g',1,1,6,'8023025600',NULL,'pcs','PANE','SFUSO GRANDE DG','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (249,'0230257','0132624','BISCOTTI AL LATTE DE GIORGIS','Biscotti al latte De Giorgis','300g',1,1,6,'8023025700',NULL,'pcs','DOLCI','BISCOTTI LATTE DG','BARCODE',NULL,40,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (250,'0230258','0132625','PANE PUGLIESE SFUSO DE GIORGIS','Pane pugliese sfuso De Giorgis','600g',1,1,6,'8023025800',NULL,'pcs','PANE','PUGLIESE SFUSO DG','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (251,'0230259','0132626','BISCOTTI BISCOTTATI F.LLI DE GIORG','Biscotti biscottati F.lli De Giorgis','250g',1,1,6,'8023025900',NULL,'pcs','DOLCI','BISCOTTATI DG','BARCODE',NULL,42,0,'Contiene glutine, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (252,'0230260','0132627','PANINI ARABO SFUSI DE GIORGIS','Panini arabo sfusi De Giorgis','200g',1,1,6,'8023026000',NULL,'pcs','PANE','ARABO SFUSI DG','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (253,'0230261','0132628','PANE TIPO ROSETTA SFUSO DE GIORGIS','Pane tipo rosetta sfuso De Giorgis','300g',1,1,6,'8023026100',NULL,'pcs','PANE','ROSETTA SFUSO DG','BARCODE',NULL,32,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (254,'0230262','0132629','BISCOTTI INTEGRALI DE GIORGIS','Biscotti integrali De Giorgis','280g',1,1,6,'8023026200',NULL,'pcs','DOLCI','INTEGRALI DG','BARCODE',NULL,38,0,'Contiene glutine integrale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (255,'0230263','0132630','BISCOTTI DELIZIA DE GIORGIS','Biscotti delizia De Giorgis','300g',1,1,6,'8023026300',NULL,'pcs','DOLCI','DELIZIA DG','BARCODE',NULL,44,0,'Contiene glutine, cioccolato',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (256,'0230264','0132631','TARALLUCCI AL VINO DE GIORGIS','Tarallucci al vino De Giorgis','250g',1,1,6,'8023026400',NULL,'pcs','DOLCI','TARALLUCCI VINO DG','BARCODE',NULL,41,0,'Contiene glutine, vino',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (257,'0230265','0132632','PANINI INTEGRALI DE GIORGIS','Panini integrali De Giorgis','200g',1,1,6,'8023026500',NULL,'pcs','PANE','INTEGRALI DG','BARCODE',NULL,36,0,'Contiene glutine integrale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (258,'0230266','0132633','PANINI INTEGRALI LS DE GORGIS','Panini integrali lievito madre','220g',1,1,6,'8023026600',NULL,'pcs','PANE','INTEGRALI LS DG','BARCODE',NULL,38,0,'Contiene glutine integrale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (259,'0230267','0132634','PEPATELLI CONF. DE GIORGIS','Pepatelli confezionati De Giorgis','180g',1,1,6,'8023026700',NULL,'pcs','DOLCI','PEPATELLI','BARCODE',NULL,45,0,'Contiene glutine, pepe, miele',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (260,'0230268','0132635','PANE GRATTUGIATO G500 DE GIORGIS','Pane grattugiato 500g De Giorgis','500g',1,1,6,'8023026800',NULL,'pcs','PANE','GRATTUGIATO DG','BARCODE',NULL,27,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (261,'0230269','0132636','PANE INTEGRALE LS FORNO BALDINI','Pane integrale lievito madre Baldini','450g',1,1,6,'8023026900',NULL,'pcs','PANE','INTEGRALE LS BALDINI','BARCODE',NULL,37,0,'Contiene glutine integrale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (262,'0230270','0132637','PANE CASARECCIO LS DE GIORGIS','Pane casareccio lievito madre DG','500g',1,1,6,'8023027000',NULL,'pcs','PANE','CASARECCIO LS DG','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (263,'0230271','0132638','PANINI AL LATTE DE GIORGIS','Panini al latte De Giorgis','250g',1,1,6,'8023027100',NULL,'pcs','PANE','LATTE DG','BARCODE',NULL,38,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (264,'0230272','0132639','NUVOLE FORNO BALDINI','Nuvole soffici Forno Baldini','200g',1,1,6,'8023027200',NULL,'pcs','PANE','NUVOLE BALDINI','BARCODE',NULL,40,0,'Contiene glutine, uova',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (265,'0230273','0132640','BANCO PANE E PASTICCERIA','Assortimento banco pane e pasticceria','1000g',1,1,6,'8023027300',NULL,'pcs','MISTO','BANCO ASSORTITO','BARCODE',NULL,42,0,'Vari allergeni',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (266,'0230274','0132641','TORTINO MAGRINI','Tortino dolce Magrini','150g',1,1,6,'8023027400',NULL,'pcs','DOLCI','TORTINO MAGRINI','BARCODE',NULL,44,0,'Contiene glutine, uova, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (267,'0230275','0132642','PANE GR.500 SFUSO BALDINI','Pane sfuso 500g Baldini','500g',1,1,6,'8023027500',NULL,'pcs','PANE','SFUSO 500G BALDINI','BARCODE',NULL,26,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (268,'0230276','0132643','PANE TIPO PUGLIESE SFUSO BALDINI','Pane pugliese sfuso Baldini','700g',1,1,6,'8023027600',NULL,'pcs','PANE','PUGLIESE SFUSO BALD','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (269,'0230277','0132644','PANE CASERECCIO SENZA SALE','Pane casareccio senza sale','450g',1,1,6,'8023027700',NULL,'pcs','PANE','SENZA SALE','BARCODE',NULL,30,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (270,'0230278','0132645','NUTELLA DONUT T2 2X60G','Nutella Donut confezione doppia','120g',1,1,6,'8023027800',NULL,'pcs','DOLCI','NUTELLA DONUT','BARCODE',NULL,47,0,'Contiene glutine, nocciole, cacao',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (271,'0230279','0132646','TORTA SACHER F.LLI DE GIORGIS','Torta Sacher F.lli De Giorgis','350g',1,1,6,'8023027900',NULL,'pcs','DOLCI','SACHER DG','BARCODE',NULL,52,0,'Contiene glutine, cioccolato, albicocche',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (272,'0230280','0132647','PANE ARABO CLASSICO 300G VECCHIO FO','Pane arabo classico Vecchio Forno','300g',1,1,6,'8023028000',NULL,'pcs','PANE','ARABO CLASSICO','BARCODE',NULL,34,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (273,'0230281','0132648','PANE ALLA ZUCCA 210G','Pane alla zucca','210g',1,1,6,'8023028100',NULL,'pcs','PANE','ZUCCA','BARCODE',NULL,39,0,'Contiene glutine, zucca',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (274,'0230282','0132649','PANE SEMI LINO/GIRASOLE 250G FORTE','Pane semi lino/girasole Forte','250g',1,1,6,'8023028200',NULL,'pcs','PANE','SEMI MISTI','BARCODE',NULL,41,0,'Contiene glutine, semi di lino, girasole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (275,'0230283','0132650','CROISSANT FRUT. ROS. INT. 5 CER. 3 MAR','Croissant frutti rossi integrali','150g',1,1,6,'8023028300',NULL,'pcs','DOLCI','CROISSANT FRUTTI','BARCODE',NULL,45,0,'Contiene glutine, frutti rossi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (276,'0230284','0132651','BOMBOLONE TRE MARIE','Bombolone Tre Marie','80g',1,1,6,'8023028400',NULL,'pcs','DOLCI','BOMBOLONE','BARCODE',NULL,43,0,'Contiene glutine, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (277,'0230285','0132652','MELANIA ALLA MELA TRE MARIE','Melania alla mela Tre Marie','90g',1,1,6,'8023028500',NULL,'pcs','DOLCI','MELANIA MELA','BARCODE',NULL,46,0,'Contiene glutine, mela',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (278,'0230286','0132653','GRECA ALLA CREMA CHANTILLY 3 MARIE','Greca crema chantilly Tre Marie','100g',1,1,6,'8023028600',NULL,'pcs','DOLCI','GRECA CHANTILLY','BARCODE',NULL,48,0,'Contiene glutine, panna, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (279,'0230287','0132654','INTRECCIO NOCCIOLA TRE MARIE','Intreccio nocciola Tre Marie','85g',1,1,6,'8023028700',NULL,'pcs','DOLCI','INTRECCIO NOCCIOLA','BARCODE',NULL,47,0,'Contiene glutine, nocciole',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (280,'0230288','0132655','PAIN AU CHOCOLAT 3 MARIE','Pain au chocolat Tre Marie','95g',1,1,6,'8023028800',NULL,'pcs','DOLCI','PAIN CHOCOLAT','BARCODE',NULL,44,0,'Contiene glutine, cioccolato',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (281,'0230289','0132656','STELLINE AL CIOCCOLATO','Stelline al cioccolato','120g',1,1,6,'8023028900',NULL,'pcs','DOLCI','STELLINE CIOCCOLATO','BARCODE',NULL,49,0,'Contiene glutine, cioccolato',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (282,'0230290','0132657','CROSTATINE AL CIOCCOLATO','Crostatine al cioccolato','140g',1,1,6,'8023029000',NULL,'pcs','DOLCI','CROSTATINE CIOCCOLATO','BARCODE',NULL,50,0,'Contiene glutine, cioccolato',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (283,'0230291','0132658','NEOLE','Neole tradizionali','200g',1,1,6,'8023029100',NULL,'pcs','DOLCI','NEOLE','BARCODE',NULL,42,0,'Contiene glutine, miele',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (284,'0230292','0132659','MARGHERITE ALL ALBICOCCA','Margherite all albicocca','160g',1,1,6,'8023029200',NULL,'pcs','DOLCI','MARGHERITE ALBICOCCA','BARCODE',NULL,47,0,'Contiene glutine, albicocche',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (285,'0230293','0132660','ANICINI','Anicini tradizionali','180g',1,1,6,'8023029300',NULL,'pcs','DOLCI','ANICINI','BARCODE',NULL,44,0,'Contiene glutine, anice',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (286,'0230294','0132661','MARGHERITE ALL AMARENA','Margherite all amarena','160g',1,1,6,'8023029400',NULL,'pcs','DOLCI','MARGHERITE AMARENA','BARCODE',NULL,48,0,'Contiene glutine, amarene',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (287,'0230295','0132662','DELIZIE ALL AMARENA','Delizie all amarena','170g',1,1,6,'8023029500',NULL,'pcs','DOLCI','DELIZIE AMARENA','BARCODE',NULL,49,0,'Contiene glutine, amarene, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (288,'0230296','0132663','CROSTATINE ALL ALBICOCCA','Crostatine all albicocca','150g',1,1,6,'8023029600',NULL,'pcs','DOLCI','CROSTATINE ALBICOCCA','BARCODE',NULL,46,0,'Contiene glutine, albicocche',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (289,'0230297','0132664','TARTELLETTES ALLA MELA 120G','Tartellettes alla mela 120g','120g',1,1,6,'8023029700',NULL,'pcs','DOLCI','TARTELLETTES MELA','BARCODE',NULL,51,0,'Contiene glutine, mela, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (290,'0230298','0132665','BISCOTTI TAGLIATI','Biscotti tagliati artigianali','250g',1,1,6,'8023029800',NULL,'pcs','DOLCI','BISCOTTI TAGLIATI','BARCODE',NULL,40,0,'Contiene glutine, burro, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (291,'0230299','0132666','CIAMBELLONE LE BRICIOLE FETTA','Ciambellone Le Briciole a fette','300g',1,1,6,'8023029900',NULL,'pcs','DOLCI','CIAMBELLONE FETTA','BARCODE',NULL,43,0,'Contiene glutine, uova, limone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (292,'0230300','0132667','TORTA MAGRINI 800GR','Torta Magrini 800g','800g',1,1,6,'8023030000',NULL,'pcs','DOLCI','TORTA MAGRINI','BARCODE',NULL,45,0,'Contiene glutine, uova, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (293,'0230301','0132668','TRECCIA NOCI PECAN TRE MARIE','Treccia noci pecan Tre Marie','200g',1,1,6,'8023030100',NULL,'pcs','DOLCI','TRECCIA PECAN','BARCODE',NULL,52,0,'Contiene glutine, noci pecan',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (294,'0230302','0132669','CROISSANT','Croissant classico','70g',1,1,6,'8023030200',NULL,'pcs','DOLCI','CROISSANT','BARCODE',NULL,41,0,'Contiene glutine, burro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (295,'0230303','0132670','GRECA ALLA CREMA CHANTILLY 3 MARIE','Greca crema chantilly Tre Marie','100g',1,1,6,'8023030300',NULL,'pcs','DOLCI','GRECA CHANTILLY2','BARCODE',NULL,48,0,'Contiene glutine, panna, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (296,'0230304','0132671','TARALLI ALLA CIPOLLA GR 400','Taralli alla cipolla 400g','400g',1,1,6,'8023030400',NULL,'pcs','SALATI','TARALLI CIPOLLA','BARCODE',NULL,37,0,'Contiene glutine, cipolla',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (297,'0230305','0132672','LINGUA ALLE PATATE 120G','Lingua alle patate 120g','120g',1,1,6,'8023030500',NULL,'pcs','SALATI','LINGUA PATATE','BARCODE',NULL,39,0,'Contiene glutine, patate',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (298,'0230306','0132673','CROCCANTELLA PATATE E ROSMAR.2.5KG','Croccantella patate rosmarino 2.5kg','2.5kg',1,1,6,'8023030600',NULL,'pcs','SALATI','CROCCANTELLA PATATE','BARCODE',NULL,32,0,'Contiene glutine, patate, rosmarino',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (299,'0230307','0132674','CROCCANTELLA MULTICEREALI 2.5KG','Croccantella multicereali 2.5kg','2.5kg',1,1,6,'8023030700',NULL,'pcs','SALATI','CROCCANTELLA CEREALI','BARCODE',NULL,34,0,'Contiene glutine, cereali misti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (300,'0230308','0132675','PASTICCIOTTO EVERYDAY','Pasticciotto Everyday','90g',1,1,6,'8023030800',NULL,'pcs','DOLCI','PASTICCIOTTO','BARCODE',NULL,46,0,'Contiene glutine, crema pasticcera',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (301,'0230309','0132676','RUSTICO LECCESE 160G','Rustico leccese 160g','160g',1,1,6,'8023030900',NULL,'pcs','SALATI','RUSTICO LECCESE','BARCODE',NULL,42,0,'Contiene glutine, pomodoro, mozzarella',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (302,'0230310','0132677','TIRAMISU 1.5KG','Tiramisù 1.5kg','1.5kg',1,1,6,'8023031000',NULL,'pcs','DOLCI','TIRAMISU GRANDE','BARCODE',NULL,55,0,'Contiene glutine, mascarpone, caffè',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (303,'0230311','0132678','TIRAMISU MONOPORZIONE 135G','Tiramisù monoporzione 135g','135g',1,1,6,'8023031100',NULL,'pcs','DOLCI','TIRAMISU MONO','BARCODE',NULL,58,0,'Contiene glutine, mascarpone, caffè',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (304,'0230312','0132679','PANE CASERECCIO SFUSO DE GIORGIS','Pane casareccio sfuso De Giorgis','600g',1,1,6,'8023031200',NULL,'pcs','PANE','CASARECCIO SFUSO DG','BARCODE',NULL,28,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (305,'0230313','0132680','PANE AFFETTATO DE GIORGIS','Pane affettato De Giorgis','450g',1,1,6,'8023031300',NULL,'pcs','PANE','AFFETTATO DG','BARCODE',NULL,33,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (306,'0230314','0132681','BISCOTTI BIANCO-NERI DE GIORGIS','Biscotti bianco-neri De Giorgis','280g',1,1,6,'8023031400',NULL,'pcs','DOLCI','BIANCO NERI DG','BARCODE',NULL,43,0,'Contiene glutine, cioccolato',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (307,'0230315','0132682','MARITOZZI F.LLI DE GIORGIS','Maritozzi F.lli De Giorgis','220g',1,1,6,'8023031500',NULL,'pcs','DOLCI','MARITOZZI DG','BARCODE',NULL,41,0,'Contiene glutine, uvetta, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (308,'0230316','0132683','CORNETTI/SACCOTTINI DE GIORGIS','Cornetti/saccottini De Giorgis','180g',1,1,6,'8023031600',NULL,'pcs','DOLCI','CORNETTI SACCOTTINI','BARCODE',NULL,44,0,'Contiene glutine, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (309,'0230317','0132684','PIZZA BIANCA SFUSA F.LLI DE GIORGI','Pizza bianca sfusa F.lli De Giorgis','200g',1,1,6,'8023031700',NULL,'pcs','SALATI','PIZZA BIANCA SFUSA','BARCODE',NULL,36,0,'Contiene glutine, olio, sale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (310,'0230318','0132685','BISCOTTI ALLE MANDORLE DE GIORGIS','Biscotti alle mandorle De Giorgis','250g',1,1,6,'8023031800',NULL,'pcs','DOLCI','MANDORLE DG','BARCODE',NULL,47,0,'Contiene glutine, mandorle',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (311,'0230319','0132686','CROSTATE F.LLI DE GIORGIS','Crostate F.lli De Giorgis','300g',1,1,6,'8023031900',NULL,'pcs','DOLCI','CROSTATE DG','BARCODE',NULL,48,0,'Contiene glutine, marmellata',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (312,'0230320','0132687','PANINI AL LATTE DE GIORGIS','Panini al latte De Giorgis','240g',1,1,6,'8023032000',NULL,'pcs','PANE','LATTE DG2','BARCODE',NULL,37,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (313,'0230321','0132688','PANE G.250-500 LS DE GIORGIS','Pane 250-500g lievito madre DG','375g',1,1,6,'8023032100',NULL,'pcs','PANE','LS MEDIO DG','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (314,'0230322','0132689','PIZZA BIANCA LS DE GIORGIS','Pizza bianca lievito madre DG','180g',1,1,6,'8023032200',NULL,'pcs','SALATI','PIZZA BIANCA LS','BARCODE',NULL,38,0,'Contiene glutine, olio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (315,'0230323','0132690','PIZZA ROSSA LS DE GIORGIS','Pizza rossa lievito madre DG','180g',1,1,6,'8023032300',NULL,'pcs','SALATI','PIZZA ROSSA LS','BARCODE',NULL,39,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (316,'0230324','0132691','PANE ALLE NOCI BALDINI','Pane alle noci Baldini','400g',1,1,6,'8023032400',NULL,'pcs','PANE','NOCI BALDINI','BARCODE',NULL,42,0,'Contiene glutine, noci',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (317,'0230325','0132692','PIZZA CROCCANTINA BALDINI','Pizza croccantina Baldini','150g',1,1,6,'8023032500',NULL,'pcs','SALATI','CROCCANTINA BALDINI','BARCODE',NULL,37,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (318,'0230326','0132693','PIZZA FARCITA FORNO BALDINI','Pizza farcita Forno Baldini','220g',1,1,6,'8023032600',NULL,'pcs','SALATI','PIZZA FARCITA','BARCODE',NULL,40,0,'Contiene glutine, verdure, formaggio',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (319,'0230327','0132694','PANINI CEREALI SFUSI DE GIORGIS','Panini cereali sfusi De Giorgis','250g',1,1,6,'8023032700',NULL,'pcs','PANE','CEREALI SFUSI DG','BARCODE',NULL,36,0,'Contiene glutine, cereali misti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (320,'0230328','0132695','SFOGLIATELLE DE GIORGIS','Sfogliatelle De Giorgis','130g',1,1,6,'8023032800',NULL,'pcs','DOLCI','SFOGLIATELLE DG','BARCODE',NULL,50,0,'Contiene glutine, ricotta, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (321,'0230329','0132696','PANINI MORBIDI/TARTARUGHE BALDINI','Panini morbidi/tartarughe Baldini','200g',1,1,6,'8023032900',NULL,'pcs','PANE','MORBIDI BALDINI','BARCODE',NULL,38,0,'Contiene glutine, latte',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (322,'0230330','0132697','PIZZA ROSSA BALDINI','Pizza rossa Baldini','170g',1,1,6,'8023033000',NULL,'pcs','SALATI','PIZZA ROSSA BALDINI','BARCODE',NULL,35,0,'Contiene glutine, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (323,'0230331','0132698','MUFFIN IL MELOGRANO','Muffin Il Melograno','80g',1,1,6,'8023033100',NULL,'pcs','DOLCI','MUFFIN MELOGRANO','BARCODE',NULL,45,0,'Contiene glutine, melograno',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (324,'0230332','0132699','PANE ALLA SEGALE 70% LIEVIT.NAT.','Pane segale 70% lievito naturale','500g',1,1,6,'8023033200',NULL,'pcs','PANE','SEGALE 70%','BARCODE',NULL,40,0,'Contiene glutine, segale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (325,'0230333','0132700','PANE AL KAMUT LIEVIT.NATURALE','Pane al kamut lievito naturale','450g',1,1,6,'8023033300',NULL,'pcs','PANE','KAMUT','BARCODE',NULL,43,0,'Contiene glutine, kamut',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (326,'0230334','0132701','PANE DI RISO LIEVIT.NATURALE','Pane di riso lievito naturale','400g',1,1,6,'8023033400',NULL,'pcs','PANE','RISO','BARCODE',NULL,45,0,'Contiene riso, senza glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (327,'0230335','0132702','PANE AI CEREALI LEVIT.NATURALE','Pane ai cereali lievito naturale','500g',1,1,6,'8023033500',NULL,'pcs','PANE','CEREALI NAT','BARCODE',NULL,38,0,'Contiene glutine, cereali misti',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (328,'0230336','0132703','PANE A FETTE C/FARINA INTEG.300G','Pane a fette farina integrale','300g',1,1,6,'8023033600',NULL,'pcs','PANE','FETTE INTEGRALE','BARCODE',NULL,36,0,'Contiene glutine integrale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (329,'0230337','0132704','PANE A FETTE CON SEGALE 300G','Pane a fette con segale','300g',1,1,6,'8023033700',NULL,'pcs','PANE','FETTE SEGALE','BARCODE',NULL,37,0,'Contiene glutine, segale',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (330,'0230338','0132705','PANE A FETTE CURCUMA 300G','Pane a fette alla curcuma','300g',1,1,6,'8023033800',NULL,'pcs','PANE','FETTE CURCUMA','BARCODE',NULL,41,0,'Contiene glutine, curcuma',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (331,'0230339','0132706','PANE A FETTE PROTEIN30 220G','Pane a fette protein30','220g',1,1,6,'8023033900',NULL,'pcs','PANE','PROTEIN30','BARCODE',NULL,48,0,'Contiene glutine, proteine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (332,'0230340','0132707','PANE A FETTE SALUS DARK 220G','Pane a fette Salus Dark','220g',1,1,6,'8023034000',NULL,'pcs','PANE','SALUS DARK','BARCODE',NULL,46,0,'Contiene glutine, cereali scuri',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (333,'0230341','0132708','GRISSINI AL SESAMO 200G CRIFILL','Grissini al sesamo Crifill','200g',1,1,6,'8023034100',NULL,'pcs','SALATI','GRISSINI SESAMO','BARCODE',NULL,39,0,'Contiene glutine, sesamo',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (334,'0230342','0132709','GRISSINI AL ROSMARINO 200G CRIFILL','Grissini al rosmarino Crifill','200g',1,1,6,'8023034200',NULL,'pcs','SALATI','GRISSINI ROSMARINO','BARCODE',NULL,38,0,'Contiene glutine, rosmarino',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (335,'0230343','0132710','GRISSINI OLIO OLIVA 200G CRIFILL','Grissini olio oliva Crifill','200g',1,1,6,'8023034300',NULL,'pcs','SALATI','GRISSINI OLIVA','BARCODE',NULL,37,0,'Contiene glutine, olio oliva',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (336,'0230344','0132711','CIAMBELLA TRE MARIE','Ciambella Tre Marie','300g',1,1,6,'8023034400',NULL,'pcs','DOLCI','CIAMBELLA TM','BARCODE',NULL,44,0,'Contiene glutine, zucchero, limone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (337,'0230345','0132712','TRECCIA NOCI PECAN TRE MARIE','Treccia noci pecan Tre Marie','200g',1,1,6,'8023034500',NULL,'pcs','DOLCI','TRECCIA PECAN TM','BARCODE',NULL,52,0,'Contiene glutine, noci pecan',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (338,'0230346','0132713','PANE ROSCA 425G','Pane Rosca 425g','425g',1,1,6,'8023034600',NULL,'pcs','PANE','ROSCA','BARCODE',NULL,35,0,'Contiene glutine',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (339,'0230347','0132714','CIACCIA TOSCANA MENCHETTI','Ciaccia toscana Menchetti','280g',1,1,6,'8023034700',NULL,'pcs','PANE','CIACCIA TOSCANA','BARCODE',NULL,39,0,'Contiene glutine, olio, erbe',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (340,'0230348','0132715','BISCOTTI TAGLIATI','Biscotti tagliati artigianali','250g',1,1,6,'8023034800',NULL,'pcs','DOLCI','BISCOTTI TAGLIATI2','BARCODE',NULL,40,0,'Contiene glutine, burro, zucchero',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (341,'0230349','0132716','CARLINI AL LIMONE','Carlini al limone','180g',1,1,6,'8023034900',NULL,'pcs','DOLCI','CARLINI LIMONE','BARCODE',NULL,47,0,'Contiene glutine, limone',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (342,'0230350','0132717','BOCCONOTTI','Bocconotti tradizionali','200g',1,1,6,'8023035000',NULL,'pcs','DOLCI','BOCCONOTTI','BARCODE',NULL,45,0,'Contiene glutine, marmellata',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (343,'0230351','0132718','SFOGLIATELLE','Sfogliatelle classiche','120g',1,1,6,'8023035100',NULL,'pcs','DOLCI','SFOGLIATELLE','BARCODE',NULL,50,0,'Contiene glutine, ricotta',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (344,'0230352','0132719','PESCHE AL CIOCCOLATO','Pesche al cioccolato','160g',1,1,6,'8023035200',NULL,'pcs','DOLCI','PESCHE CIOCCOLATO','BARCODE',NULL,49,0,'Contiene glutine, cioccolato, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (345,'0230353','0132720','MIX DI FAZZOLETTI','Mix di fazzoletti dolci','220g',1,1,6,'8023035300',NULL,'pcs','DOLCI','MIX FAZZOLETTI','BARCODE',NULL,44,0,'Contiene glutine, varie creme',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (346,'0230354','0132721','FOCACCINA 5 MORSI OLIVE/POM.180G','Focaccina 5 morsi olive/pomodoro','180g',1,1,6,'8023035400',NULL,'pcs','SALATI','FOCACCINA OLIVE','BARCODE',NULL,41,0,'Contiene glutine, olive, pomodoro',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (347,'0230355','0132722','FOCACCINA 5 MORSI STRACCHINO 180G','Focaccina 5 morsi stracchino','180g',1,1,6,'8023035500',NULL,'pcs','SALATI','FOCACCINA STRACCHINO','BARCODE',NULL,43,0,'Contiene glutine, stracchino',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (348,'0230356','0132723','ECLAIR CIOCCOLATO 45G (16PZX6)','Eclair cioccolato 45g confezione','45g',1,1,6,'8023035600',NULL,'pcs','DOLCI','ECLAIR CIOCCOLATO','BARCODE',NULL,53,0,'Contiene glutine, cioccolato, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (349,'0230357','0132724','ECLAIR VANIGLIA 45G (16PZX6)','Eclair vaniglia 45g confezione','45g',1,1,6,'8023035700',NULL,'pcs','DOLCI','ECLAIR VANIGLIA','BARCODE',NULL,52,0,'Contiene glutine, vaniglia, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (350,'0230358','0132725','TARTELLETTES AI LAMPONI 110G 5PZX6','Tartellettes ai lamponi 110g','110g',1,1,6,'8023035800',NULL,'pcs','DOLCI','TARTELLETTES LAMPONI','BARCODE',NULL,54,0,'Contiene glutine, lamponi, crema',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "products" VALUES (351,'0230197','0132564','TARTELLETTES MERINGA/FR.ROSSI 100G','Tartellette meringa frutti rossi','100g',1,1,6,'8023019700',NULL,'pcs','DOLCI','TARTELLETTE','BARCODE',NULL,52,0,'Contiene glutine, uova, frutti rossi',NULL,NULL,NULL,NULL,0,NULL,0,1,'2025-09-25 14:38:08','2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (1,'PROV001','Distribuzione Alimentare Nord','supplier','Marco Bianchi',NULL,'ordini@dan.it','+39 02 1111111','Via Industria 10','Milano','20100','Italy','IT01234567890',NULL,NULL,30,2.5,'',1,'2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (2,'PROV002','Bevande Express','supplier','Anna Rossi',NULL,'vendite@bevande.it','+39 02 2222222','Via Logistica 25','Milano','20121','Italy','IT09876543210',NULL,NULL,15,3,'',1,'2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (3,'PROV003','Fresh Food Supply','supplier','Giuseppe Romano',NULL,'fresh@food.it','+39 02 5555555','Via Freschezza 15','Milano','20124','Italy','IT11223344556',NULL,NULL,7,1.5,'',1,'2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (4,'PROV004','Logistica Express','delivery','Roberto Verdi',NULL,'trasporti@logex.it','+39 02 6666666','Via Trasporti 88','Milano','20125','Italy','IT55667788990',NULL,NULL,0,0,'',1,'2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (5,'PROV005','Surgelati Premium','supplier','Chiara Neri',NULL,'vendite@surgelatipremium.it','+39 02 7777777','Via Fredda 33','Milano','20126','Italy','IT99887766554',NULL,NULL,21,2,'',1,'2025-09-25 14:38:08');
INSERT INTO "providers" VALUES (6,'PROV006','Panificio Industriale','supplier','Luca Conti',NULL,'ordini@panificioind.it','+39 02 8888888','Via Farina 12','Milano','20127','Italy','IT44556677889',NULL,NULL,14,4,'',1,'2025-09-25 14:38:08');
INSERT INTO "roles" VALUES (1,'admin','System Administrator - Full access',0);
INSERT INTO "roles" VALUES (2,'manager','Store Manager - Management access',1);
INSERT INTO "roles" VALUES (3,'supervisor','Department Supervisor - Limited management',2);
INSERT INTO "roles" VALUES (4,'user','Store Employee - Basic operations',3);
INSERT INTO "supermarket_departments" VALUES (1,'FRESH','Fresh Products','fresh',NULL,'2025-09-25 14:37:46');
INSERT INTO "supermarket_departments" VALUES (2,'FROZEN','Frozen Foods','frozen',NULL,'2025-09-25 14:37:46');
INSERT INTO "supermarket_departments" VALUES (3,'DRY','Dry Goods','dry',NULL,'2025-09-25 14:37:46');
INSERT INTO "supermarket_departments" VALUES (4,'BEVERAGE','Beverages','beverages',NULL,'2025-09-25 14:37:46');
INSERT INTO "user_permissions" VALUES (1,'system.admin','Full system administration',0);
INSERT INTO "user_permissions" VALUES (2,'users.manage','Manage user accounts',0);
INSERT INTO "user_permissions" VALUES (3,'system.config','System configuration',0);
INSERT INTO "user_permissions" VALUES (4,'products.manage','Manage product catalog',1);
INSERT INTO "user_permissions" VALUES (5,'inventory.manage','Manage inventory operations',1);
INSERT INTO "user_permissions" VALUES (6,'reports.financial','View financial reports',1);
INSERT INTO "user_permissions" VALUES (7,'employees.manage','Manage employee accounts',1);
INSERT INTO "user_permissions" VALUES (8,'sales.supervise','Supervise sales operations',2);
INSERT INTO "user_permissions" VALUES (9,'inventory.view','View inventory status',2);
INSERT INTO "user_permissions" VALUES (10,'reports.operational','View operational reports',2);
INSERT INTO "user_permissions" VALUES (11,'clients.manage','Manage client accounts',2);
INSERT INTO "user_permissions" VALUES (12,'sales.process','Process sales transactions',3);
INSERT INTO "user_permissions" VALUES (13,'products.read','Read product information',3);
INSERT INTO "user_permissions" VALUES (14,'clients.read','Read client information',3);
INSERT INTO "user_permissions" VALUES (15,'inventory.check','Check inventory levels',3);
INSERT INTO "users" VALUES (1,'f47ac10b-58cc-4372-a567-0e02b2c3d479','mario.admin','mario.admin@aptismart.com','Mario','Rossi',1,1,'2025-09-25 14:37:29');
INSERT INTO "users" VALUES (2,'6ba7b810-9dad-11d1-80b4-00c04fd430c8','lucia.manager','lucia.manager@aptismart.com','Lucia','Bianchi',2,1,'2025-09-25 14:37:29');
INSERT INTO "users" VALUES (3,'6ba7b811-9dad-11d1-80b4-00c04fd430c8','giuseppe.supervisor','giuseppe.supervisor@aptismart.com','Giuseppe','Verdi',3,1,'2025-09-25 14:37:29');
INSERT INTO "users" VALUES (4,'6ba7b812-9dad-11d1-80b4-00c04fd430c8','anna.employee','anna.employee@aptismart.com','Anna','Neri',4,1,'2025-09-25 14:37:29');
CREATE INDEX IF NOT EXISTS "idx_business_costs_category" ON "business_costs" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "idx_business_costs_date" ON "business_costs" (
	"cost_date"
);
CREATE INDEX IF NOT EXISTS "idx_business_costs_status" ON "business_costs" (
	"payment_status"
);
CREATE INDEX IF NOT EXISTS "idx_business_revenues_category" ON "business_revenues" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "idx_business_revenues_date" ON "business_revenues" (
	"revenue_date"
);
CREATE INDEX IF NOT EXISTS "idx_business_revenues_status" ON "business_revenues" (
	"payment_status"
);
CREATE INDEX IF NOT EXISTS "idx_clients_category_status" ON "clients" (
	"client_category",
	"client_status"
);
CREATE INDEX IF NOT EXISTS "idx_clients_code" ON "clients" (
	"client_code"
);
CREATE INDEX IF NOT EXISTS "idx_clients_email" ON "clients" (
	"email"
);
CREATE INDEX IF NOT EXISTS "idx_contracts_type_active" ON "employee_contracts" (
	"contract_type",
	"is_active"
);
CREATE INDEX IF NOT EXISTS "idx_counter_departments_code" ON "counter_departments" (
	"counter_code"
);
CREATE INDEX IF NOT EXISTS "idx_employee_contracts_employee_id" ON "employee_contracts" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "idx_employee_contracts_number" ON "employee_contracts" (
	"contract_number"
);
CREATE INDEX IF NOT EXISTS "idx_employees_code" ON "employees" (
	"employee_code"
);
CREATE INDEX IF NOT EXISTS "idx_employees_email" ON "employees" (
	"email"
);
CREATE INDEX IF NOT EXISTS "idx_employees_location" ON "employees" (
	"location_id"
);
CREATE INDEX IF NOT EXISTS "idx_financial_categories_code" ON "financial_categories" (
	"category_code"
);
CREATE INDEX IF NOT EXISTS "idx_financial_categories_scope" ON "financial_categories" (
	"category_scope"
);
CREATE INDEX IF NOT EXISTS "idx_locations_active_type" ON "locations" (
	"is_active",
	"location_type"
);
CREATE INDEX IF NOT EXISTS "idx_locations_code" ON "locations" (
	"location_code"
);
CREATE INDEX IF NOT EXISTS "idx_loyalty_cards_client" ON "loyalty_cards" (
	"client_id"
);
CREATE INDEX IF NOT EXISTS "idx_loyalty_cards_number" ON "loyalty_cards" (
	"card_number"
);
CREATE INDEX IF NOT EXISTS "idx_products_barcode" ON "products" (
	"barcode"
);
CREATE INDEX IF NOT EXISTS "idx_products_code" ON "products" (
	"product_code"
);
CREATE INDEX IF NOT EXISTS "idx_products_department_counter" ON "products" (
	"department_id",
	"counter_id"
);
CREATE INDEX IF NOT EXISTS "idx_providers_code" ON "providers" (
	"provider_code"
);
CREATE INDEX IF NOT EXISTS "idx_roles_level" ON "roles" (
	"role_level"
);
CREATE INDEX IF NOT EXISTS "idx_sessions_session_id" ON "keycloak_sessions" (
	"session_id"
);
CREATE INDEX IF NOT EXISTS "idx_sessions_user_id" ON "keycloak_sessions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "idx_user_permissions_level" ON "user_permissions" (
	"required_role_level"
);
CREATE INDEX IF NOT EXISTS "idx_user_permissions_name" ON "user_permissions" (
	"permission_name"
);
CREATE INDEX IF NOT EXISTS "idx_users_keycloak_id" ON "users" (
	"keycloak_user_id"
);
CREATE INDEX IF NOT EXISTS "idx_users_role_id" ON "users" (
	"role_id"
);
CREATE INDEX IF NOT EXISTS "idx_users_username" ON "users" (
	"username"
);
COMMIT;
