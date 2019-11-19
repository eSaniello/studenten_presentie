-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2019 at 02:57 AM
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
-- Table structure for table `presenties`
--

CREATE TABLE `presenties` (
  `id` int(11) NOT NULL,
  `student_nr` varchar(255) NOT NULL,
  `vak_code` varchar(255) NOT NULL,
  `presentie` varchar(255) NOT NULL,
  `blok` int(10) NOT NULL,
  `datum` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `presenties`
--

INSERT INTO `presenties` (`id`, `student_nr`, `vak_code`, `presentie`, `blok`, `datum`) VALUES
(7, '156241762581', 'EN', 'afwezig', 2, '2019-11-11'),
(9, '76453', 'PR', 'aanwezig', 4, '2019-11-10'),
(10, '54765658', 'PR', 'aanwezig', 3, '2019-11-12'),
(11, '25769268', 'OND', 'afwezig', 5, '2019-11-11'),
(12, '156241762581', 'DA', 'afwezig', 6, '2019-11-11'),
(13, '256472', 'EN', 'aanwezig', 3, '2019-11-18');

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
('156241762581', 'Shaniel', 'Samadhan', '2016', '4', 'ICT'),
('256472', 'Raishrie', 'Ambika', '2016', '4', 'ICT'),
('25769268', 'Lorenzo', 'Amania', '2016', '4', 'ICT'),
('52636354', 'Kedescha', 'Ansoe', '2016', '4', 'ICT'),
('5476466', 'Joel', 'Naarendorp', '2017', '3', 'ICT'),
('54765658', 'Kenson', 'Latchmansing', '2016', '4', 'ICT'),
('76453', 'Andojo', 'Mack', '2016', '4', 'ICT'),
('7i65735', 'Alisha', 'Nasibdar', '2016', '4', 'ICT'),
('9867858672', 'Lesley', 'Uiterloo', '2017', '3', 'ICT');

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
('DA', 'Distributed Applications'),
('EN', 'Engels'),
('IK', 'Informatiekunde'),
('NL', 'Nederlands'),
('OND', 'Ondernemerschap'),
('PM', 'Projectmanagement'),
('PR', 'Projecten'),
('UML', 'UML'),
('WK', 'Wiskunde');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `presenties`
--
ALTER TABLE `presenties`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_nr` (`student_nr`),
  ADD KEY `vak_code` (`vak_code`);

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

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `presenties`
--
ALTER TABLE `presenties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `presenties`
--
ALTER TABLE `presenties`
  ADD CONSTRAINT `presenties_ibfk_1` FOREIGN KEY (`student_nr`) REFERENCES `studenten` (`student_nr`),
  ADD CONSTRAINT `presenties_ibfk_2` FOREIGN KEY (`vak_code`) REFERENCES `vakken` (`vak_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
