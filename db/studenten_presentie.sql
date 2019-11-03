-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2019 at 08:56 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studenten_presentie`
--

-- --------------------------------------------------------

--
-- Table structure for table `studenten`
--

CREATE TABLE `studenten` (
  `student_nr` varchar(255) NOT NULL,
  `voornaam` varchar(255) NOT NULL,
  `achternaam` varchar(255) NOT NULL,
  `cohort` varchar(255) NOT NULL,
  `leerjaar` varchar(255) NOT NULL,
  `studierichting` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studenten`
--

INSERT INTO `studenten` (`student_nr`, `voornaam`, `achternaam`, `cohort`, `leerjaar`, `studierichting`) VALUES
('1111111', 'Shaniel', 'Samadhan', '2019-2020', '4', 'ICT');

-- --------------------------------------------------------

--
-- Table structure for table `vakken`
--

CREATE TABLE `vakken` (
  `vak_code` varchar(255) NOT NULL,
  `naam` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vakken`
--

INSERT INTO `vakken` (`vak_code`, `naam`) VALUES
('1', 'Wiskunde'),
('2', 'UML');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `studenten`
--
ALTER TABLE `studenten`
  ADD PRIMARY KEY (`student_nr`);

--
-- Indexes for table `vakken`
--
ALTER TABLE `vakken`
  ADD PRIMARY KEY (`vak_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
