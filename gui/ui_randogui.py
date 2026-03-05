# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randogui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QComboBox,
    QFontComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QListView,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 759)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setSizeIncrement(QSize(0, 0))
        self.tabWidget.setToolTipDuration(-6)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tab_setup = QWidget()
        self.tab_setup.setObjectName("tab_setup")
        self.verticalLayout_27 = QVBoxLayout(self.tab_setup)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.vlay_files = QVBoxLayout()
        self.vlay_files.setObjectName("vlay_files")
        self.hlay_output = QHBoxLayout()
        self.hlay_output.setObjectName("hlay_output")
        self.label_output = QLabel(self.tab_setup)
        self.label_output.setObjectName("label_output")
        self.label_output.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.hlay_output.addWidget(self.label_output)

        self.output_folder = QLineEdit(self.tab_setup)
        self.output_folder.setObjectName("output_folder")

        self.hlay_output.addWidget(self.output_folder)

        self.ouput_folder_browse_button = QPushButton(self.tab_setup)
        self.ouput_folder_browse_button.setObjectName("ouput_folder_browse_button")

        self.hlay_output.addWidget(self.ouput_folder_browse_button)

        self.vlay_files.addLayout(self.hlay_output)

        self.vlay_plando = QVBoxLayout()
        self.vlay_plando.setObjectName("vlay_plando")
        self.hlay_plando_file = QHBoxLayout()
        self.hlay_plando_file.setObjectName("hlay_plando_file")
        self.option_plando = QCheckBox(self.tab_setup)
        self.option_plando.setObjectName("option_plando")

        self.hlay_plando_file.addWidget(self.option_plando)

        self.plando_file = QLineEdit(self.tab_setup)
        self.plando_file.setObjectName("plando_file")

        self.hlay_plando_file.addWidget(self.plando_file)

        self.plando_file_browse = QPushButton(self.tab_setup)
        self.plando_file_browse.setObjectName("plando_file_browse")

        self.hlay_plando_file.addWidget(self.plando_file_browse)

        self.vlay_plando.addLayout(self.hlay_plando_file)

        self.vlay_files.addLayout(self.vlay_plando)

        self.verticalLayout_27.addLayout(self.vlay_files)

        self.hlay_setup_options = QHBoxLayout()
        self.hlay_setup_options.setObjectName("hlay_setup_options")
        self.box_additional_files = QGroupBox(self.tab_setup)
        self.box_additional_files.setObjectName("box_additional_files")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.box_additional_files.sizePolicy().hasHeightForWidth()
        )
        self.box_additional_files.setSizePolicy(sizePolicy2)
        self.box_additional_files.setFlat(False)
        self.verticalLayout_22 = QVBoxLayout(self.box_additional_files)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.vlay_additional_files = QVBoxLayout()
        self.vlay_additional_files.setObjectName("vlay_additional_files")
        self.option_no_spoiler_log = QCheckBox(self.box_additional_files)
        self.option_no_spoiler_log.setObjectName("option_no_spoiler_log")

        self.vlay_additional_files.addWidget(self.option_no_spoiler_log)

        self.option_json_spoiler = QCheckBox(self.box_additional_files)
        self.option_json_spoiler.setObjectName("option_json_spoiler")

        self.vlay_additional_files.addWidget(self.option_json_spoiler)

        self.option_out_placement_file = QCheckBox(self.box_additional_files)
        self.option_out_placement_file.setObjectName("option_out_placement_file")

        self.vlay_additional_files.addWidget(self.option_out_placement_file)

        self.vspace_additional_files = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_additional_files.addItem(self.vspace_additional_files)

        self.verticalLayout_22.addLayout(self.vlay_additional_files)

        self.hlay_setup_options.addWidget(self.box_additional_files)

        self.box_advanced = QGroupBox(self.tab_setup)
        self.box_advanced.setObjectName("box_advanced")
        sizePolicy2.setHeightForWidth(
            self.box_advanced.sizePolicy().hasHeightForWidth()
        )
        self.box_advanced.setSizePolicy(sizePolicy2)
        self.verticalLayout_23 = QVBoxLayout(self.box_advanced)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.vlay_advanced = QVBoxLayout()
        self.vlay_advanced.setObjectName("vlay_advanced")
        self.option_dry_run = QCheckBox(self.box_advanced)
        self.option_dry_run.setObjectName("option_dry_run")

        self.vlay_advanced.addWidget(self.option_dry_run)

        self.vspace_advanced = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_advanced.addItem(self.vspace_advanced)

        self.verticalLayout_23.addLayout(self.vlay_advanced)

        self.hlay_setup_options.addWidget(self.box_advanced)

        self.box_cosmetics = QGroupBox(self.tab_setup)
        self.box_cosmetics.setObjectName("box_cosmetics")
        sizePolicy2.setHeightForWidth(
            self.box_cosmetics.sizePolicy().hasHeightForWidth()
        )
        self.box_cosmetics.setSizePolicy(sizePolicy2)
        self.verticalLayout_24 = QVBoxLayout(self.box_cosmetics)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.vlay_cosmetics = QVBoxLayout()
        self.vlay_cosmetics.setObjectName("vlay_cosmetics")
        self.option_cryptic_location_hints = QCheckBox(self.box_cosmetics)
        self.option_cryptic_location_hints.setObjectName(
            "option_cryptic_location_hints"
        )

        self.vlay_cosmetics.addWidget(self.option_cryptic_location_hints)

        self.option_lightning_skyward_strike = QCheckBox(self.box_cosmetics)
        self.option_lightning_skyward_strike.setObjectName(
            "option_lightning_skyward_strike"
        )

        self.vlay_cosmetics.addWidget(self.option_lightning_skyward_strike)

        self.option_starry_skies = QCheckBox(self.box_cosmetics)
        self.option_starry_skies.setObjectName("option_starry_skies")

        self.vlay_cosmetics.addWidget(self.option_starry_skies)

        self.hlay_star_count = QHBoxLayout()
        self.hlay_star_count.setObjectName("hlay_star_count")
        self.label_for_option_star_count = QLabel(self.box_cosmetics)
        self.label_for_option_star_count.setObjectName("label_for_option_star_count")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_for_option_star_count.sizePolicy().hasHeightForWidth()
        )
        self.label_for_option_star_count.setSizePolicy(sizePolicy3)

        self.hlay_star_count.addWidget(self.label_for_option_star_count)

        self.option_star_count = QSpinBox(self.box_cosmetics)
        self.option_star_count.setObjectName("option_star_count")
        self.option_star_count.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.option_star_count.sizePolicy().hasHeightForWidth()
        )
        self.option_star_count.setSizePolicy(sizePolicy4)
        self.option_star_count.setMaximum(32767)
        self.option_star_count.setSingleStep(100)

        self.hlay_star_count.addWidget(self.option_star_count)

        self.vlay_cosmetics.addLayout(self.hlay_star_count)

        self.label_for_option_interface = QLabel(self.box_cosmetics)
        self.label_for_option_interface.setObjectName("label_for_option_interface")

        self.vlay_cosmetics.addWidget(self.label_for_option_interface)

        self.option_interface = QComboBox(self.box_cosmetics)
        self.option_interface.setObjectName("option_interface")

        self.vlay_cosmetics.addWidget(self.option_interface)

        self.vspace_cosmetics = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_cosmetics.addItem(self.vspace_cosmetics)

        self.verticalLayout_24.addLayout(self.vlay_cosmetics)

        self.hlay_setup_options.addWidget(self.box_cosmetics)

        self.box_music_rando = QGroupBox(self.tab_setup)
        self.box_music_rando.setObjectName("box_music_rando")
        sizePolicy2.setHeightForWidth(
            self.box_music_rando.sizePolicy().hasHeightForWidth()
        )
        self.box_music_rando.setSizePolicy(sizePolicy2)
        self.verticalLayout_25 = QVBoxLayout(self.box_music_rando)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.vlay_music_rando = QVBoxLayout()
        self.vlay_music_rando.setObjectName("vlay_music_rando")
        self.vlay_music_rando_option = QVBoxLayout()
        self.vlay_music_rando_option.setObjectName("vlay_music_rando_option")
        self.label_for_option_music_rando = QLabel(self.box_music_rando)
        self.label_for_option_music_rando.setObjectName("label_for_option_music_rando")

        self.vlay_music_rando_option.addWidget(self.label_for_option_music_rando)

        self.option_music_rando = QComboBox(self.box_music_rando)
        self.option_music_rando.setObjectName("option_music_rando")

        self.vlay_music_rando_option.addWidget(self.option_music_rando)

        self.vlay_music_rando.addLayout(self.vlay_music_rando_option)

        self.option_cutoff_gameover_music = QCheckBox(self.box_music_rando)
        self.option_cutoff_gameover_music.setObjectName("option_cutoff_gameover_music")

        self.vlay_music_rando.addWidget(self.option_cutoff_gameover_music)

        self.option_allow_custom_music = QCheckBox(self.box_music_rando)
        self.option_allow_custom_music.setObjectName("option_allow_custom_music")

        self.vlay_music_rando.addWidget(self.option_allow_custom_music)

        self.option_no_enemy_music = QCheckBox(self.box_music_rando)
        self.option_no_enemy_music.setObjectName("option_no_enemy_music")

        self.vlay_music_rando.addWidget(self.option_no_enemy_music)

        self.vspace_music_rando = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_music_rando.addItem(self.vspace_music_rando)

        self.verticalLayout_25.addLayout(self.vlay_music_rando)

        self.hlay_setup_options.addWidget(self.box_music_rando)

        self.box = QGroupBox(self.tab_setup)
        self.box.setObjectName("box")
        sizePolicy2.setHeightForWidth(self.box.sizePolicy().hasHeightForWidth())
        self.box.setSizePolicy(sizePolicy2)
        self.verticalLayout_28 = QVBoxLayout(self.box)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.vspace_10 = QSpacerItem(
            20, 342, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_28.addItem(self.vspace_10)

        self.hlay_setup_options.addWidget(self.box)

        self.verticalLayout_27.addLayout(self.hlay_setup_options)

        self.hlay_presets_rs = QHBoxLayout()
        self.hlay_presets_rs.setObjectName("hlay_presets_rs")
        self.box_presets = QGroupBox(self.tab_setup)
        self.box_presets.setObjectName("box_presets")
        sizePolicy2.setHeightForWidth(self.box_presets.sizePolicy().hasHeightForWidth())
        self.box_presets.setSizePolicy(sizePolicy2)
        self.verticalLayout_26 = QVBoxLayout(self.box_presets)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.vlay_presets = QVBoxLayout()
        self.vlay_presets.setObjectName("vlay_presets")
        self.label_presets = QLabel(self.box_presets)
        self.label_presets.setObjectName("label_presets")
        self.label_presets.setWordWrap(False)

        self.vlay_presets.addWidget(self.label_presets)

        self.presets_list = QComboBox(self.box_presets)
        self.presets_list.setObjectName("presets_list")

        self.vlay_presets.addWidget(self.presets_list)

        self.hlay_presets_controls = QHBoxLayout()
        self.hlay_presets_controls.setObjectName("hlay_presets_controls")
        self.load_preset = QPushButton(self.box_presets)
        self.load_preset.setObjectName("load_preset")

        self.hlay_presets_controls.addWidget(self.load_preset)

        self.save_preset = QPushButton(self.box_presets)
        self.save_preset.setObjectName("save_preset")

        self.hlay_presets_controls.addWidget(self.save_preset)

        self.delete_preset = QPushButton(self.box_presets)
        self.delete_preset.setObjectName("delete_preset")

        self.hlay_presets_controls.addWidget(self.delete_preset)

        self.vlay_presets.addLayout(self.hlay_presets_controls)

        self.verticalLayout_26.addLayout(self.vlay_presets)

        self.hlay_presets_rs.addWidget(self.box_presets)

        self.box_rs = QGroupBox(self.tab_setup)
        self.box_rs.setObjectName("box_rs")
        sizePolicy2.setHeightForWidth(self.box_rs.sizePolicy().hasHeightForWidth())
        self.box_rs.setSizePolicy(sizePolicy2)
        self.horizontalLayout_12 = QHBoxLayout(self.box_rs)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.vlay_rs = QVBoxLayout()
        self.vlay_rs.setObjectName("vlay_rs")
        self.hlay_rs_controls = QHBoxLayout()
        self.hlay_rs_controls.setObjectName("hlay_rs_controls")
        self.option_random_settings = QCheckBox(self.box_rs)
        self.option_random_settings.setObjectName("option_random_settings")

        self.hlay_rs_controls.addWidget(self.option_random_settings)

        self.option_random_cosmetics = QCheckBox(self.box_rs)
        self.option_random_cosmetics.setObjectName("option_random_cosmetics")

        self.hlay_rs_controls.addWidget(self.option_random_cosmetics)

        self.vlay_rs.addLayout(self.hlay_rs_controls)

        self.hlay_rs_settings = QHBoxLayout()
        self.hlay_rs_settings.setObjectName("hlay_rs_settings")
        self.vlay_rs_weighting = QVBoxLayout()
        self.vlay_rs_weighting.setObjectName("vlay_rs_weighting")
        self.label_random_settings_weighting = QLabel(self.box_rs)
        self.label_random_settings_weighting.setObjectName(
            "label_random_settings_weighting"
        )

        self.vlay_rs_weighting.addWidget(self.label_random_settings_weighting)

        self.option_random_settings_weighting = QComboBox(self.box_rs)
        self.option_random_settings_weighting.setObjectName(
            "option_random_settings_weighting"
        )

        self.vlay_rs_weighting.addWidget(self.option_random_settings_weighting)

        self.hlay_rs_settings.addLayout(self.vlay_rs_weighting)

        self.vlay_rs_progression_locations = QVBoxLayout()
        self.vlay_rs_progression_locations.setObjectName(
            "vlay_rs_progression_locations"
        )
        self.label_progression_locations = QLabel(self.box_rs)
        self.label_progression_locations.setObjectName("label_progression_locations")

        self.vlay_rs_progression_locations.addWidget(self.label_progression_locations)

        self.edit_progression_groups = QPushButton(self.box_rs)
        self.edit_progression_groups.setObjectName("edit_progression_groups")

        self.vlay_rs_progression_locations.addWidget(self.edit_progression_groups)

        self.hlay_rs_settings.addLayout(self.vlay_rs_progression_locations)

        self.vlay_rs.addLayout(self.hlay_rs_settings)

        self.horizontalLayout_12.addLayout(self.vlay_rs)

        self.hlay_presets_rs.addWidget(self.box_rs)

        self.verticalLayout_27.addLayout(self.hlay_presets_rs)

        self.tabWidget.addTab(self.tab_setup, "")
        self.tab_randomization_settings = QWidget()
        self.tab_randomization_settings.setObjectName("tab_randomization_settings")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_randomization_settings)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.box_completion = QGroupBox(self.tab_randomization_settings)
        self.box_completion.setObjectName("box_completion")
        sizePolicy2.setHeightForWidth(
            self.box_completion.sizePolicy().hasHeightForWidth()
        )
        self.box_completion.setSizePolicy(sizePolicy2)
        self.verticalLayout_18 = QVBoxLayout(self.box_completion)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.vlay_completion = QVBoxLayout()
        self.vlay_completion.setObjectName("vlay_completion")
        self.vlay_got_start = QVBoxLayout()
        self.vlay_got_start.setObjectName("vlay_got_start")
        self.label_for_option_got_starting_state = QLabel(self.box_completion)
        self.label_for_option_got_starting_state.setObjectName(
            "label_for_option_got_starting_state"
        )

        self.vlay_got_start.addWidget(self.label_for_option_got_starting_state)

        self.option_got_starting_state = QComboBox(self.box_completion)
        self.option_got_starting_state.setObjectName("option_got_starting_state")

        self.vlay_got_start.addWidget(self.option_got_starting_state)

        self.vlay_completion.addLayout(self.vlay_got_start)

        self.vlay_sword_req = QVBoxLayout()
        self.vlay_sword_req.setObjectName("vlay_sword_req")
        self.label_for_option_got_sword_requirement = QLabel(self.box_completion)
        self.label_for_option_got_sword_requirement.setObjectName(
            "label_for_option_got_sword_requirement"
        )

        self.vlay_sword_req.addWidget(self.label_for_option_got_sword_requirement)

        self.option_got_sword_requirement = QComboBox(self.box_completion)
        self.option_got_sword_requirement.setObjectName("option_got_sword_requirement")

        self.vlay_sword_req.addWidget(self.option_got_sword_requirement)

        self.vlay_completion.addLayout(self.vlay_sword_req)

        self.vlay_got_dungeon_req = QVBoxLayout()
        self.vlay_got_dungeon_req.setObjectName("vlay_got_dungeon_req")
        self.label_for_option_got_dungeon_requirement = QLabel(self.box_completion)
        self.label_for_option_got_dungeon_requirement.setObjectName(
            "label_for_option_got_dungeon_requirement"
        )

        self.vlay_got_dungeon_req.addWidget(
            self.label_for_option_got_dungeon_requirement
        )

        self.option_got_dungeon_requirement = QComboBox(self.box_completion)
        self.option_got_dungeon_requirement.setObjectName(
            "option_got_dungeon_requirement"
        )

        self.vlay_got_dungeon_req.addWidget(self.option_got_dungeon_requirement)

        self.vlay_completion.addLayout(self.vlay_got_dungeon_req)

        self.hlay_req_dungeons = QHBoxLayout()
        self.hlay_req_dungeons.setObjectName("hlay_req_dungeons")
        self.label_for_option_required_dungeon_count = QLabel(self.box_completion)
        self.label_for_option_required_dungeon_count.setObjectName(
            "label_for_option_required_dungeon_count"
        )

        self.hlay_req_dungeons.addWidget(self.label_for_option_required_dungeon_count)

        self.option_required_dungeon_count = QSpinBox(self.box_completion)
        self.option_required_dungeon_count.setObjectName(
            "option_required_dungeon_count"
        )
        self.option_required_dungeon_count.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.option_required_dungeon_count.sizePolicy().hasHeightForWidth()
        )
        self.option_required_dungeon_count.setSizePolicy(sizePolicy5)
        self.option_required_dungeon_count.setMaximumSize(QSize(41, 16777215))
        self.option_triforce_required.setObjectName("option_triforce_required")

        self.vlay_completion.addWidget(self.option_triforce_required)

        self.vlay_triforce_shuffle = QVBoxLayout()
        self.vlay_triforce_shuffle.setObjectName("vlay_triforce_shuffle")
        self.label_for_option_triforce_shuffle = QLabel(self.box_completion)
        self.label_for_option_triforce_shuffle.setObjectName(
            "label_for_option_triforce_shuffle"
        )

        self.vlay_triforce_shuffle.addWidget(self.label_for_option_triforce_shuffle)

        self.option_triforce_shuffle = QComboBox(self.box_completion)
        self.option_triforce_shuffle.setObjectName("option_triforce_shuffle")

        self.vlay_triforce_shuffle.addWidget(self.option_triforce_shuffle)

        self.vlay_completion.addLayout(self.vlay_triforce_shuffle)

        self.option_imp_2 = QCheckBox(self.box_completion)
        self.option_imp_2.setObjectName("option_imp_2")

        self.vlay_completion.addWidget(self.option_imp_2)

        self.option_horde = QCheckBox(self.box_completion)
        self.option_horde.setObjectName("option_horde")

        self.vlay_completion.addWidget(self.option_horde)

        self.option_g3 = QCheckBox(self.box_completion)
        self.option_g3.setObjectName("option_g3")

        self.vlay_completion.addWidget(self.option_g3)

        self.option_demise = QCheckBox(self.box_completion)
        self.option_demise.setObjectName("option_demise")

        self.vlay_completion.addWidget(self.option_demise)

        self.hlay_demise_count = QHBoxLayout()
        self.hlay_demise_count.setObjectName("hlay_demise_count")
        self.label_for_option_demise_count = QLabel(self.box_completion)
        self.label_for_option_demise_count.setObjectName(
            "label_for_option_demise_count"
        )

        self.hlay_demise_count.addWidget(self.label_for_option_demise_count)

        self.option_demise_count = QSpinBox(self.box_completion)
        self.option_demise_count.setObjectName("option_demise_count")
        sizePolicy5.setHeightForWidth(
            self.option_demise_count.sizePolicy().hasHeightForWidth()
        )
        self.option_demise_count.setSizePolicy(sizePolicy5)
        self.option_demise_count.setMaximumSize(QSize(41, 16777215))

        self.hlay_demise_count.addWidget(self.option_demise_count)

        self.vlay_completion.addLayout(self.hlay_demise_count)

        self.vspace_completion = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_completion.addItem(self.vspace_completion)

        self.verticalLayout_18.addLayout(self.vlay_completion)

        self.horizontalLayout_7.addWidget(self.box_completion)

        self.box_open = QGroupBox(self.tab_randomization_settings)
        self.box_open.setObjectName("box_open")
        sizePolicy2.setHeightForWidth(self.box_open.sizePolicy().hasHeightForWidth())
        self.box_open.setSizePolicy(sizePolicy2)
        self.verticalLayout_21 = QVBoxLayout(self.box_open)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.vlay_open = QVBoxLayout()
        self.vlay_open.setObjectName("vlay_open")
        self.vlay_open_thunderhead = QVBoxLayout()
        self.vlay_open_thunderhead.setObjectName("vlay_open_thunderhead")
        self.label_for_option_open_thunderhead = QLabel(self.box_open)
        self.label_for_option_open_thunderhead.setObjectName(
            "label_for_option_open_thunderhead"
        )

        self.vlay_open_thunderhead.addWidget(self.label_for_option_open_thunderhead)

        self.option_open_thunderhead = QComboBox(self.box_open)
        self.option_open_thunderhead.setObjectName("option_open_thunderhead")

        self.vlay_open_thunderhead.addWidget(self.option_open_thunderhead)

        self.vlay_open.addLayout(self.vlay_open_thunderhead)

        self.option_open_et = QCheckBox(self.box_open)
        self.option_open_et.setObjectName("option_open_et")

        self.vlay_open.addWidget(self.option_open_et)

        self.vlay_open_lmf = QVBoxLayout()
        self.vlay_open_lmf.setObjectName("vlay_open_lmf")
        self.label_for_option_open_lmf = QLabel(self.box_open)
        self.label_for_option_open_lmf.setObjectName("label_for_option_open_lmf")

        self.vlay_open_lmf.addWidget(self.label_for_option_open_lmf)

        self.option_open_lmf = QComboBox(self.box_open)
        self.option_open_lmf.setObjectName("option_open_lmf")

        self.vlay_open_lmf.addWidget(self.option_open_lmf)

        self.vlay_open.addLayout(self.vlay_open_lmf)

        self.label_for_option_open_lake_floria = QLabel(self.box_open)
        self.label_for_option_open_lake_floria.setObjectName(
            "label_for_option_open_lake_floria"
        )

        self.vlay_open.addWidget(self.label_for_option_open_lake_floria)

        self.option_open_lake_floria = QComboBox(self.box_open)
        self.option_open_lake_floria.setObjectName("option_open_lake_floria")

        self.vlay_open.addWidget(self.option_open_lake_floria)

        self.option_random_puzzles = QCheckBox(self.box_open)
        self.option_random_puzzles.setObjectName("option_random_puzzles")

        self.vlay_open.addWidget(self.option_random_puzzles)

        self.vspace_open = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_open.addItem(self.vspace_open)

        self.verticalLayout_21.addLayout(self.vlay_open)

        self.horizontalLayout_7.addWidget(self.box_open)

        self.box_shuffles = QGroupBox(self.tab_randomization_settings)
        self.box_shuffles.setObjectName("box_shuffles")
        sizePolicy2.setHeightForWidth(
            self.box_shuffles.sizePolicy().hasHeightForWidth()
        )
        self.box_shuffles.setSizePolicy(sizePolicy2)
        self.verticalLayout_17 = QVBoxLayout(self.box_shuffles)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.vlay_shuffles = QVBoxLayout()
        self.vlay_shuffles.setObjectName("vlay_shuffles")
        self.vlay_batreaux_counts = QVBoxLayout()
        self.vlay_batreaux_counts.setObjectName("vlay_batreaux_counts")
        self.label_for_option_batreaux_counts = QLabel(self.box_shuffles)
        self.label_for_option_batreaux_counts.setObjectName(
            "label_for_option_batreaux_counts"
        )

        self.vlay_batreaux_counts.addWidget(self.label_for_option_batreaux_counts)

        self.option_batreaux_counts = QComboBox(self.box_shuffles)
        self.option_batreaux_counts.setObjectName("option_batreaux_counts")

        self.vlay_batreaux_counts.addWidget(self.option_batreaux_counts)

        self.vlay_shuffles.addLayout(self.vlay_batreaux_counts)

        self.option_shopsanity = QCheckBox(self.box_shuffles)
        self.option_shopsanity.setObjectName("option_shopsanity")

        self.vlay_shuffles.addWidget(self.option_shopsanity)

        self.option_rupeesanity = QCheckBox(self.box_shuffles)
        self.option_rupeesanity.setObjectName("option_rupeesanity")

        self.vlay_shuffles.addWidget(self.option_rupeesanity)

        self.option_tadtonesanity = QCheckBox(self.box_shuffles)
        self.option_tadtonesanity.setObjectName("option_tadtonesanity")

        self.vlay_shuffles.addWidget(self.option_tadtonesanity)

        self.vspace_shuffles = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_shuffles.addItem(self.vspace_shuffles)

        self.verticalLayout_17.addLayout(self.vlay_shuffles)

        self.horizontalLayout_7.addWidget(self.box_shuffles)

        self.box_entrance_rando = QGroupBox(self.tab_randomization_settings)
        self.box_entrance_rando.setObjectName("box_entrance_rando")
        sizePolicy2.setHeightForWidth(
            self.box_entrance_rando.sizePolicy().hasHeightForWidth()
        )
        self.box_entrance_rando.setSizePolicy(sizePolicy2)
        self.verticalLayout_20 = QVBoxLayout(self.box_entrance_rando)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.vlay_entrance_rando = QVBoxLayout()
        self.vlay_entrance_rando.setObjectName("vlay_entrance_rando")
        self.vlay_dungeon_entrance_rando = QVBoxLayout()
        self.vlay_dungeon_entrance_rando.setObjectName("vlay_dungeon_entrance_rando")
        self.label_for_option_randomize_entrances = QLabel(self.box_entrance_rando)
        self.label_for_option_randomize_entrances.setObjectName(
            "label_for_option_randomize_entrances"
        )

        self.vlay_dungeon_entrance_rando.addWidget(
            self.label_for_option_randomize_entrances
        )

        self.option_randomize_entrances = QComboBox(self.box_entrance_rando)
        self.option_randomize_entrances.setObjectName("option_randomize_entrances")

        self.vlay_dungeon_entrance_rando.addWidget(self.option_randomize_entrances)

        self.vlay_entrance_rando.addLayout(self.vlay_dungeon_entrance_rando)

        self.option_randomize_trials = QCheckBox(self.box_entrance_rando)
        self.option_randomize_trials.setObjectName("option_randomize_trials")

        self.vlay_entrance_rando.addWidget(self.option_randomize_trials)

        self.label_for_option_random_start_entrance = QLabel(self.box_entrance_rando)
        self.label_for_option_random_start_entrance.setObjectName(
            "label_for_option_random_start_entrance"
        )

        self.vlay_entrance_rando.addWidget(self.label_for_option_random_start_entrance)

        self.option_random_start_entrance = QComboBox(self.box_entrance_rando)
        self.option_random_start_entrance.setObjectName("option_random_start_entrance")

        self.vlay_entrance_rando.addWidget(self.option_random_start_entrance)

        self.option_limit_start_entrance = QCheckBox(self.box_entrance_rando)
        self.option_limit_start_entrance.setObjectName("option_limit_start_entrance")

        self.vlay_entrance_rando.addWidget(self.option_limit_start_entrance)

        self.option_random_start_statues = QCheckBox(self.box_entrance_rando)
        self.option_random_start_statues.setObjectName("option_random_start_statues")

        self.vlay_entrance_rando.addWidget(self.option_random_start_statues)

        self.vspace_entrance_rando = QSpacerItem(
            20, 70, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding
        )

        self.vlay_entrance_rando.addItem(self.vspace_entrance_rando)

        self.verticalLayout_20.addLayout(self.vlay_entrance_rando)

        self.horizontalLayout_7.addWidget(self.box_entrance_rando)

        self.box_dungeons = QGroupBox(self.tab_randomization_settings)
        self.box_dungeons.setObjectName("box_dungeons")
        sizePolicy2.setHeightForWidth(
            self.box_dungeons.sizePolicy().hasHeightForWidth()
        )
        self.box_dungeons.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.box_dungeons)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.vlay_dungeons = QVBoxLayout()
        self.vlay_dungeons.setObjectName("vlay_dungeons")
        self.vlay_map_shuffle = QVBoxLayout()
        self.vlay_map_shuffle.setObjectName("vlay_map_shuffle")
        self.label_for_option_map_mode = QLabel(self.box_dungeons)
        self.label_for_option_map_mode.setObjectName("label_for_option_map_mode")

        self.vlay_map_shuffle.addWidget(self.label_for_option_map_mode)

        self.option_map_mode = QComboBox(self.box_dungeons)
        self.option_map_mode.setObjectName("option_map_mode")

        self.vlay_map_shuffle.addWidget(self.option_map_mode)

        self.vlay_dungeons.addLayout(self.vlay_map_shuffle)

        self.vlay_small_key_shuffle = QVBoxLayout()
        self.vlay_small_key_shuffle.setObjectName("vlay_small_key_shuffle")
        self.label_for_option_small_key_mode = QLabel(self.box_dungeons)
        self.label_for_option_small_key_mode.setObjectName(
            "label_for_option_small_key_mode"
        )

        self.vlay_small_key_shuffle.addWidget(self.label_for_option_small_key_mode)

        self.option_small_key_mode = QComboBox(self.box_dungeons)
        self.option_small_key_mode.setObjectName("option_small_key_mode")

        self.vlay_small_key_shuffle.addWidget(self.option_small_key_mode)

        self.vlay_dungeons.addLayout(self.vlay_small_key_shuffle)

        self.vlay_boss_key_shuffle = QVBoxLayout()
        self.vlay_boss_key_shuffle.setObjectName("vlay_boss_key_shuffle")
        self.label_for_option_boss_key_mode = QLabel(self.box_dungeons)
        self.label_for_option_boss_key_mode.setObjectName(
            "label_for_option_boss_key_mode"
        )

        self.vlay_boss_key_shuffle.addWidget(self.label_for_option_boss_key_mode)

        self.option_boss_key_mode = QComboBox(self.box_dungeons)
        self.option_boss_key_mode.setObjectName("option_boss_key_mode")

        self.vlay_boss_key_shuffle.addWidget(self.option_boss_key_mode)

        self.vlay_dungeons.addLayout(self.vlay_boss_key_shuffle)

        self.option_empty_unrequired_dungeons = QCheckBox(self.box_dungeons)
        self.option_empty_unrequired_dungeons.setObjectName(
            "option_empty_unrequired_dungeons"
        )

        self.vlay_dungeons.addWidget(self.option_empty_unrequired_dungeons)

        self.vlay_sword_reward = QVBoxLayout()
        self.vlay_sword_reward.setObjectName("vlay_sword_reward")
        self.label_for_sword_dungeon_reward = QLabel(self.box_dungeons)
        self.label_for_sword_dungeon_reward.setObjectName(
            "label_for_sword_dungeon_reward"
        )

        self.vlay_sword_reward.addWidget(self.label_for_sword_dungeon_reward)

        self.option_sword_dungeon_reward = QComboBox(self.box_dungeons)
        self.option_sword_dungeon_reward.setObjectName("option_sword_dungeon_reward")

        self.vlay_sword_reward.addWidget(self.option_sword_dungeon_reward)

        self.vlay_dungeons.addLayout(self.vlay_sword_reward)

        self.option_randomize_boss_key_puzzles = QCheckBox(self.box_dungeons)
        self.option_randomize_boss_key_puzzles.setObjectName(
            "option_randomize_boss_key_puzzles"
        )

        self.vlay_dungeons.addWidget(self.option_randomize_boss_key_puzzles)

        self.label_for_dungeon_patches = QLabel(self.box_dungeons)
        self.label_for_dungeon_patches.setObjectName("label_for_dungeon_patches")

        self.vlay_dungeons.addWidget(self.label_for_dungeon_patches)

        self.option_fs_lava_flow = QCheckBox(self.box_dungeons)
        self.option_fs_lava_flow.setObjectName("option_fs_lava_flow")

        self.vlay_dungeons.addWidget(self.option_fs_lava_flow)

        self.vlay_open_dungeon_shortcuts = QVBoxLayout()
        self.vlay_open_dungeon_shortcuts.setObjectName("vlay_open_dungeon_shortcuts")
        self.label_for_dungeon_shortcuts = QLabel(self.box_dungeons)
        self.label_for_dungeon_shortcuts.setObjectName("label_for_dungeon_shortcuts")

        self.vlay_open_dungeon_shortcuts.addWidget(self.label_for_dungeon_shortcuts)

        self.option_open_dungeon_shortcuts = QComboBox(self.box_dungeons)
        self.option_open_dungeon_shortcuts.setObjectName(
            "option_open_dungeon_shortcuts"
        )

        self.vlay_open_dungeon_shortcuts.addWidget(self.option_open_dungeon_shortcuts)

        self.vlay_dungeons.addLayout(self.vlay_open_dungeon_shortcuts)

        self.vspace_dungeons = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_dungeons.addItem(self.vspace_dungeons)

        self.verticalLayout_19.addLayout(self.vlay_dungeons)

        self.horizontalLayout_7.addWidget(self.box_dungeons)

        self.tabWidget.addTab(self.tab_randomization_settings, "")
        self.tab_additional_settings = QWidget()
        self.tab_additional_settings.setObjectName("tab_additional_settings")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_additional_settings)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.box_convenience_tweaks = QGroupBox(self.tab_additional_settings)
        self.box_convenience_tweaks.setObjectName("box_convenience_tweaks")
        sizePolicy2.setHeightForWidth(
            self.box_convenience_tweaks.sizePolicy().hasHeightForWidth()
        )
        self.box_convenience_tweaks.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.box_convenience_tweaks)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vlay_convenience_tweaks = QVBoxLayout()
        self.vlay_convenience_tweaks.setObjectName("vlay_convenience_tweaks")
        self.option_fill_dowsing_on_white_sword = QCheckBox(self.box_convenience_tweaks)
        self.option_fill_dowsing_on_white_sword.setObjectName(
            "option_fill_dowsing_on_white_sword"
        )

        self.vlay_convenience_tweaks.addWidget(self.option_fill_dowsing_on_white_sword)

        self.option_full_wallet_upgrades = QCheckBox(self.box_convenience_tweaks)
        self.option_full_wallet_upgrades.setObjectName("option_full_wallet_upgrades")

        self.vlay_convenience_tweaks.addWidget(self.option_full_wallet_upgrades)

        self.vspace_convenience_tweaks = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_convenience_tweaks.addItem(self.vspace_convenience_tweaks)

        self.verticalLayout_4.addLayout(self.vlay_convenience_tweaks)

        self.horizontalLayout_4.addWidget(self.box_convenience_tweaks)

        self.box_vanilla_tweaks = QGroupBox(self.tab_additional_settings)
        self.box_vanilla_tweaks.setObjectName("box_vanilla_tweaks")
        sizePolicy2.setHeightForWidth(
            self.box_vanilla_tweaks.sizePolicy().hasHeightForWidth()
        )
        self.box_vanilla_tweaks.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.box_vanilla_tweaks)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.vlay_vanilla_tweaks = QVBoxLayout()
        self.vlay_vanilla_tweaks.setObjectName("vlay_vanilla_tweaks")
        self.label_for_option_bit_patches = QLabel(self.box_vanilla_tweaks)
        self.label_for_option_bit_patches.setObjectName("label_for_option_bit_patches")

        self.vlay_vanilla_tweaks.addWidget(self.label_for_option_bit_patches)

        self.option_bit_patches = QComboBox(self.box_vanilla_tweaks)
        self.option_bit_patches.setObjectName("option_bit_patches")

        self.vlay_vanilla_tweaks.addWidget(self.option_bit_patches)

        self.hlay_peatrice_conversations = QHBoxLayout()
        self.hlay_peatrice_conversations.setObjectName("hlay_peatrice_conversations")
        self.label_for_option_peatrice_conversations = QLabel(self.box_vanilla_tweaks)
        self.label_for_option_peatrice_conversations.setObjectName(
            "label_for_option_peatrice_conversations"
        )

        self.hlay_peatrice_conversations.addWidget(
            self.label_for_option_peatrice_conversations
        )

        self.option_peatrice_conversations = QSpinBox(self.box_vanilla_tweaks)
        self.option_peatrice_conversations.setObjectName(
            "option_peatrice_conversations"
        )
        sizePolicy5.setHeightForWidth(
            self.option_peatrice_conversations.sizePolicy().hasHeightForWidth()
        )
        self.option_peatrice_conversations.setSizePolicy(sizePolicy5)

        self.hlay_peatrice_conversations.addWidget(self.option_peatrice_conversations)

        self.vlay_vanilla_tweaks.addLayout(self.hlay_peatrice_conversations)

        self.vspace_vanilla_tweaks = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_vanilla_tweaks.addItem(self.vspace_vanilla_tweaks)

        self.verticalLayout_8.addLayout(self.vlay_vanilla_tweaks)

        self.horizontalLayout_4.addWidget(self.box_vanilla_tweaks)

        self.box_item_pool = QGroupBox(self.tab_additional_settings)
        self.box_item_pool.setObjectName("box_item_pool")
        sizePolicy2.setHeightForWidth(
            self.box_item_pool.sizePolicy().hasHeightForWidth()
        )
        self.box_item_pool.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.box_item_pool)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vlay_item_pool = QVBoxLayout()
        self.vlay_item_pool.setObjectName("vlay_item_pool")
        self.vlay_rupoor_mode = QVBoxLayout()
        self.vlay_rupoor_mode.setObjectName("vlay_rupoor_mode")
        self.option_gondo_upgrades = QCheckBox(self.box_item_pool)
        self.option_gondo_upgrades.setObjectName("option_gondo_upgrades")

        self.vlay_rupoor_mode.addWidget(self.option_gondo_upgrades)

        self.label_for_option_rupoor_mode = QLabel(self.box_item_pool)
        self.label_for_option_rupoor_mode.setObjectName("label_for_option_rupoor_mode")

        self.vlay_rupoor_mode.addWidget(self.label_for_option_rupoor_mode)

        self.option_rupoor_mode = QComboBox(self.box_item_pool)
        self.option_rupoor_mode.setObjectName("option_rupoor_mode")

        self.vlay_rupoor_mode.addWidget(self.option_rupoor_mode)

        self.vspace_item_pool = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_rupoor_mode.addItem(self.vspace_item_pool)

        self.vlay_item_pool.addLayout(self.vlay_rupoor_mode)

        self.verticalLayout_6.addLayout(self.vlay_item_pool)

        self.horizontalLayout_4.addWidget(self.box_item_pool)

        self.box_silent_realms = QGroupBox(self.tab_additional_settings)
        self.box_silent_realms.setObjectName("box_silent_realms")
        sizePolicy2.setHeightForWidth(
            self.box_silent_realms.sizePolicy().hasHeightForWidth()
        )
        self.box_silent_realms.setSizePolicy(sizePolicy2)
        self.horizontalLayout_10 = QHBoxLayout(self.box_silent_realms)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vlay_silent_realms = QVBoxLayout()
        self.vlay_silent_realms.setObjectName("vlay_silent_realms")
        self.verticalLayout_trialshuffle = QVBoxLayout()
        self.verticalLayout_trialshuffle.setObjectName("verticalLayout_trialshuffle")
        self.label_for_option_shuffle_trial_objects = QLabel(self.box_silent_realms)
        self.label_for_option_shuffle_trial_objects.setObjectName(
            "label_for_option_shuffle_trial_objects"
        )
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.label_for_option_shuffle_trial_objects.sizePolicy().hasHeightForWidth()
        )
        self.label_for_option_shuffle_trial_objects.setSizePolicy(sizePolicy6)

        self.verticalLayout_trialshuffle.addWidget(
            self.label_for_option_shuffle_trial_objects
        )

        self.option_shuffle_trial_objects = QComboBox(self.box_silent_realms)
        self.option_shuffle_trial_objects.setObjectName("option_shuffle_trial_objects")

        self.verticalLayout_trialshuffle.addWidget(self.option_shuffle_trial_objects)

        self.vlay_silent_realms.addLayout(self.verticalLayout_trialshuffle)

        self.option_treasuresanity_in_silent_realms = QCheckBox(self.box_silent_realms)
        self.option_treasuresanity_in_silent_realms.setObjectName(
            "option_treasuresanity_in_silent_realms"
        )

        self.vlay_silent_realms.addWidget(self.option_treasuresanity_in_silent_realms)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.label_for_option_trial_treasure_amount = QLabel(self.box_silent_realms)
        self.label_for_option_trial_treasure_amount.setObjectName(
            "label_for_option_trial_treasure_amount"
        )

        self.horizontalLayout_9.addWidget(self.label_for_option_trial_treasure_amount)

        self.option_trial_treasure_amount = QSpinBox(self.box_silent_realms)
        self.option_trial_treasure_amount.setObjectName("option_trial_treasure_amount")
        self.option_trial_treasure_amount.setMaximumSize(QSize(48, 16777215))
        self.option_trial_treasure_amount.setMinimum(1)
        self.option_trial_treasure_amount.setMaximum(10)

        self.horizontalLayout_9.addWidget(self.option_trial_treasure_amount)

        self.vlay_silent_realms.addLayout(self.horizontalLayout_9)

        self.vspace_silent_realms = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_silent_realms.addItem(self.vspace_silent_realms)

        self.horizontalLayout_10.addLayout(self.vlay_silent_realms)

        self.horizontalLayout_4.addWidget(self.box_silent_realms)

        self.box_heromode_changes = QGroupBox(self.tab_additional_settings)
        self.box_heromode_changes.setObjectName("box_heromode_changes")
        sizePolicy2.setHeightForWidth(
            self.box_heromode_changes.sizePolicy().hasHeightForWidth()
        )
        self.box_heromode_changes.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.box_heromode_changes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vlay_heromode_changes = QVBoxLayout()
        self.vlay_heromode_changes.setObjectName("vlay_heromode_changes")
        self.option_upgraded_skyward_strike = QCheckBox(self.box_heromode_changes)
        self.option_upgraded_skyward_strike.setObjectName(
            "option_upgraded_skyward_strike"
        )

        self.vlay_heromode_changes.addWidget(self.option_upgraded_skyward_strike)

        self.option_fast_air_meter = QCheckBox(self.box_heromode_changes)
        self.option_fast_air_meter.setObjectName("option_fast_air_meter")

        self.vlay_heromode_changes.addWidget(self.option_fast_air_meter)

        self.option_enable_heart_drops = QCheckBox(self.box_heromode_changes)
        self.option_enable_heart_drops.setObjectName("option_enable_heart_drops")

        self.vlay_heromode_changes.addWidget(self.option_enable_heart_drops)

        self.hlay_damage_multiplier = QHBoxLayout()
        self.hlay_damage_multiplier.setObjectName("hlay_damage_multiplier")
        self.label_for_option_damage_multiplier = QLabel(self.box_heromode_changes)
        self.label_for_option_damage_multiplier.setObjectName(
            "label_for_option_damage_multiplier"
        )

        self.hlay_damage_multiplier.addWidget(self.label_for_option_damage_multiplier)

        self.option_damage_multiplier = QSpinBox(self.box_heromode_changes)
        self.option_damage_multiplier.setObjectName("option_damage_multiplier")
        sizePolicy5.setHeightForWidth(
            self.option_damage_multiplier.sizePolicy().hasHeightForWidth()
        )
        self.option_damage_multiplier.setSizePolicy(sizePolicy5)
        self.option_damage_multiplier.setMaximumSize(QSize(41, 16777215))
        self.option_damage_multiplier.setMinimum(1)
        self.option_damage_multiplier.setMaximum(255)

        self.hlay_damage_multiplier.addWidget(self.option_damage_multiplier)

        self.vlay_heromode_changes.addLayout(self.hlay_damage_multiplier)

        self.vspace_heromode_changes = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_heromode_changes.addItem(self.vspace_heromode_changes)

        self.verticalLayout_5.addLayout(self.vlay_heromode_changes)

        self.horizontalLayout_4.addWidget(self.box_heromode_changes)

        self.tabWidget.addTab(self.tab_additional_settings, "")
        self.tab_logic_settings = QWidget()
        self.tab_logic_settings.setObjectName("tab_logic_settings")
        sizePolicy.setHeightForWidth(
            self.tab_logic_settings.sizePolicy().hasHeightForWidth()
        )
        self.tab_logic_settings.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.tab_logic_settings)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vlay_logic_settings = QVBoxLayout()
        self.vlay_logic_settings.setObjectName("vlay_logic_settings")
        self.hlay_misc_logic_settings = QHBoxLayout()
        self.hlay_misc_logic_settings.setObjectName("hlay_misc_logic_settings")
        self.label_for_option_logic_mode = QLabel(self.tab_logic_settings)
        self.label_for_option_logic_mode.setObjectName("label_for_option_logic_mode")

        self.hlay_misc_logic_settings.addWidget(self.label_for_option_logic_mode)

        self.option_logic_mode = QComboBox(self.tab_logic_settings)
        self.option_logic_mode.setObjectName("option_logic_mode")

        self.hlay_misc_logic_settings.addWidget(self.option_logic_mode)

        self.edit_tricks = QPushButton(self.tab_logic_settings)
        self.edit_tricks.setObjectName("edit_tricks")

        self.hlay_misc_logic_settings.addWidget(self.edit_tricks)

        self.hspace_misc_logic_settings = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.hlay_misc_logic_settings.addItem(self.hspace_misc_logic_settings)

        self.vlay_logic_settings.addLayout(self.hlay_misc_logic_settings)

        self.vlay_exclude_locations = QVBoxLayout()
        self.vlay_exclude_locations.setSpacing(6)
        self.vlay_exclude_locations.setObjectName("vlay_exclude_locations")
        self.hlay_exclude_locations_body = QHBoxLayout()
        self.hlay_exclude_locations_body.setObjectName("hlay_exclude_locations_body")
        self.vlay_include_locations = QVBoxLayout()
        self.vlay_include_locations.setObjectName("vlay_include_locations")
        self.label_include_locations = QLabel(self.tab_logic_settings)
        self.label_include_locations.setObjectName("label_include_locations")

        self.vlay_include_locations.addWidget(self.label_include_locations)

        self.hlay_include_filters = QHBoxLayout()
        self.hlay_include_filters.setObjectName("hlay_include_filters")
        self.include_category_filters = QComboBox(self.tab_logic_settings)
        self.include_category_filters.setObjectName("include_category_filters")

        self.hlay_include_filters.addWidget(self.include_category_filters)

        self.included_free_search = QLineEdit(self.tab_logic_settings)
        self.included_free_search.setObjectName("included_free_search")
        sizePolicy4.setHeightForWidth(
            self.included_free_search.sizePolicy().hasHeightForWidth()
        )
        self.included_free_search.setSizePolicy(sizePolicy4)
        self.included_free_search.setClearButtonEnabled(True)

        self.hlay_include_filters.addWidget(self.included_free_search)

        self.vlay_include_locations.addLayout(self.hlay_include_filters)

        self.included_locations = QListView(self.tab_logic_settings)
        self.included_locations.setObjectName("included_locations")
        self.included_locations.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.included_locations.setProperty("showDropIndicator", False)
        self.included_locations.setSelectionMode(QAbstractItemView.MultiSelection)
        self.included_locations.setSelectionRectVisible(False)

        self.vlay_include_locations.addWidget(self.included_locations)

        self.hlay_exclude_locations_body.addLayout(self.vlay_include_locations)

        self.vlay_exclude_locations_controls = QVBoxLayout()
        self.vlay_exclude_locations_controls.setObjectName(
            "vlay_exclude_locations_controls"
        )
        self.vspace_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_exclude_locations_controls.addItem(self.vspace_9)

        self.include_location = QPushButton(self.tab_logic_settings)
        self.include_location.setObjectName("include_location")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.include_location.sizePolicy().hasHeightForWidth()
        )
        self.include_location.setSizePolicy(sizePolicy7)

        self.vlay_exclude_locations_controls.addWidget(self.include_location)

        self.vspace_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_exclude_locations_controls.addItem(self.vspace_7)

        self.exclude_location = QPushButton(self.tab_logic_settings)
        self.exclude_location.setObjectName("exclude_location")
        sizePolicy7.setHeightForWidth(
            self.exclude_location.sizePolicy().hasHeightForWidth()
        )
        self.exclude_location.setSizePolicy(sizePolicy7)

        self.vlay_exclude_locations_controls.addWidget(self.exclude_location)

        self.vspace_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_exclude_locations_controls.addItem(self.vspace_8)

        self.hlay_exclude_locations_body.addLayout(self.vlay_exclude_locations_controls)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_exclude_locations = QLabel(self.tab_logic_settings)
        self.label_exclude_locations.setObjectName("label_exclude_locations")

        self.verticalLayout_30.addWidget(self.label_exclude_locations)

        self.hlay_exclude_filters = QHBoxLayout()
        self.hlay_exclude_filters.setObjectName("hlay_exclude_filters")
        self.exclude_category_filters = QComboBox(self.tab_logic_settings)
        self.exclude_category_filters.setObjectName("exclude_category_filters")

        self.hlay_exclude_filters.addWidget(self.exclude_category_filters)

        self.excluded_free_search = QLineEdit(self.tab_logic_settings)
        self.excluded_free_search.setObjectName("excluded_free_search")
        sizePolicy4.setHeightForWidth(
            self.excluded_free_search.sizePolicy().hasHeightForWidth()
        )
        self.excluded_free_search.setSizePolicy(sizePolicy4)
        self.excluded_free_search.setClearButtonEnabled(True)

        self.hlay_exclude_filters.addWidget(self.excluded_free_search)

        self.verticalLayout_30.addLayout(self.hlay_exclude_filters)

        self.excluded_locations = QListView(self.tab_logic_settings)
        self.excluded_locations.setObjectName("excluded_locations")
        self.excluded_locations.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.excluded_locations.setProperty("showDropIndicator", False)
        self.excluded_locations.setSelectionMode(QAbstractItemView.MultiSelection)
        self.excluded_locations.setSelectionRectVisible(False)

        self.verticalLayout_30.addWidget(self.excluded_locations)

        self.hlay_exclude_locations_body.addLayout(self.verticalLayout_30)

        self.vlay_exclude_locations.addLayout(self.hlay_exclude_locations_body)

        self.vlay_logic_settings.addLayout(self.vlay_exclude_locations)

        self.horizontalLayout.addLayout(self.vlay_logic_settings)

        self.tabWidget.addTab(self.tab_logic_settings, "")
        self.tab_hints = QWidget()
        self.tab_hints.setObjectName("tab_hints")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_hints)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.box_stone_hints = QGroupBox(self.tab_hints)
        self.box_stone_hints.setObjectName("box_stone_hints")
        sizePolicy2.setHeightForWidth(
            self.box_stone_hints.sizePolicy().hasHeightForWidth()
        )
        self.box_stone_hints.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.box_stone_hints)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.vlay_stone_hints = QVBoxLayout()
        self.vlay_stone_hints.setObjectName("vlay_stone_hints")
        self.vlay_hint_distro = QVBoxLayout()
        self.vlay_hint_distro.setObjectName("vlay_hint_distro")
        self.label_for_option_hint_distribution = QLabel(self.box_stone_hints)
        self.label_for_option_hint_distribution.setObjectName(
            "label_for_option_hint_distribution"
        )

        self.vlay_hint_distro.addWidget(self.label_for_option_hint_distribution)

        self.option_hint_distribution = QComboBox(self.box_stone_hints)
        self.option_hint_distribution.setObjectName("option_hint_distribution")

        self.vlay_hint_distro.addWidget(self.option_hint_distribution)

        self.vlay_stone_hints.addLayout(self.vlay_hint_distro)

        self.option_cube_sots = QCheckBox(self.box_stone_hints)
        self.option_cube_sots.setObjectName("option_cube_sots")

        self.vlay_stone_hints.addWidget(self.option_cube_sots)

        self.option_precise_item = QCheckBox(self.box_stone_hints)
        self.option_precise_item.setObjectName("option_precise_item")

        self.vlay_stone_hints.addWidget(self.option_precise_item)

        self.option_hint_importance = QCheckBox(self.box_stone_hints)
        self.option_hint_importance.setObjectName("option_hint_importance")

        self.vlay_stone_hints.addWidget(self.option_hint_importance)

        self.vspace_stone_hints = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_stone_hints.addItem(self.vspace_stone_hints)

        self.verticalLayout_12.addLayout(self.vlay_stone_hints)

        self.horizontalLayout_6.addWidget(self.box_stone_hints)

        self.box_other_hints = QGroupBox(self.tab_hints)
        self.box_other_hints.setObjectName("box_other_hints")
        sizePolicy2.setHeightForWidth(
            self.box_other_hints.sizePolicy().hasHeightForWidth()
        )
        self.box_other_hints.setSizePolicy(sizePolicy2)
        self.verticalLayout_13 = QVBoxLayout(self.box_other_hints)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.vlay_other_hints = QVBoxLayout()
        self.vlay_other_hints.setObjectName("vlay_other_hints")
        self.vlay_song_hints = QVBoxLayout()
        self.vlay_song_hints.setObjectName("vlay_song_hints")
        self.label_for_option_song_hints = QLabel(self.box_other_hints)
        self.label_for_option_song_hints.setObjectName("label_for_option_song_hints")

        self.vlay_song_hints.addWidget(self.label_for_option_song_hints)

        self.option_song_hints = QComboBox(self.box_other_hints)
        self.option_song_hints.setObjectName("option_song_hints")

        self.vlay_song_hints.addWidget(self.option_song_hints)

        self.vlay_other_hints.addLayout(self.vlay_song_hints)

        self.option_impa_sot_hint = QCheckBox(self.box_other_hints)
        self.option_impa_sot_hint.setObjectName("option_impa_sot_hint")

        self.vlay_other_hints.addWidget(self.option_impa_sot_hint)

        self.vlay_chest_dowsing = QVBoxLayout()
        self.vlay_chest_dowsing.setObjectName("vlay_chest_dowsing")
        self.label_for_option_chest_dowsing = QLabel(self.box_other_hints)
        self.label_for_option_chest_dowsing.setObjectName(
            "label_for_option_chest_dowsing"
        )

        self.vlay_chest_dowsing.addWidget(self.label_for_option_chest_dowsing)

        self.option_chest_dowsing = QComboBox(self.box_other_hints)
        self.option_chest_dowsing.setObjectName("option_chest_dowsing")

        self.vlay_chest_dowsing.addWidget(self.option_chest_dowsing)

        self.vlay_other_hints.addLayout(self.vlay_chest_dowsing)

        self.option_dungeon_dowsing = QCheckBox(self.box_other_hints)
        self.option_dungeon_dowsing.setObjectName("option_dungeon_dowsing")

        self.vlay_other_hints.addWidget(self.option_dungeon_dowsing)

        self.vspace_other_hints = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_other_hints.addItem(self.vspace_other_hints)

        self.verticalLayout_13.addLayout(self.vlay_other_hints)

        self.horizontalLayout_6.addWidget(self.box_other_hints)

        self.box_4 = QGroupBox(self.tab_hints)
        self.box_4.setObjectName("box_4")
        sizePolicy2.setHeightForWidth(self.box_4.sizePolicy().hasHeightForWidth())
        self.box_4.setSizePolicy(sizePolicy2)
        self.verticalLayout_14 = QVBoxLayout(self.box_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.vspace_4 = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.vspace_4)

        self.horizontalLayout_6.addWidget(self.box_4)

        self.box_5 = QGroupBox(self.tab_hints)
        self.box_5.setObjectName("box_5")
        sizePolicy2.setHeightForWidth(self.box_5.sizePolicy().hasHeightForWidth())
        self.box_5.setSizePolicy(sizePolicy2)
        self.verticalLayout_15 = QVBoxLayout(self.box_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.vspace_5 = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.vspace_5)

        self.horizontalLayout_6.addWidget(self.box_5)

        self.box_6 = QGroupBox(self.tab_hints)
        self.box_6.setObjectName("box_6")
        sizePolicy2.setHeightForWidth(self.box_6.sizePolicy().hasHeightForWidth())
        self.box_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_16 = QVBoxLayout(self.box_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.vspace_6 = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.vspace_6)

        self.horizontalLayout_6.addWidget(self.box_6)

        self.tabWidget.addTab(self.tab_hints, "")
        self.tab_starting_items = QWidget()
        self.tab_starting_items.setObjectName("tab_starting_items")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_starting_items)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.box_starting_items = QGroupBox(self.tab_starting_items)
        self.box_starting_items.setObjectName("box_starting_items")
        sizePolicy.setHeightForWidth(
            self.box_starting_items.sizePolicy().hasHeightForWidth()
        )
        self.box_starting_items.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.box_starting_items)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vlay_randomized_items_section = QVBoxLayout()
        self.vlay_randomized_items_section.setObjectName(
            "vlay_randomized_items_section"
        )
        self.label_randomized_items = QLabel(self.box_starting_items)
        self.label_randomized_items.setObjectName("label_randomized_items")

        self.vlay_randomized_items_section.addWidget(self.label_randomized_items)

        self.randomized_items_free_search = QLineEdit(self.box_starting_items)
        self.randomized_items_free_search.setObjectName("randomized_items_free_search")
        self.randomized_items_free_search.setClearButtonEnabled(True)

        self.vlay_randomized_items_section.addWidget(self.randomized_items_free_search)

        self.randomized_items = QListView(self.box_starting_items)
        self.randomized_items.setObjectName("randomized_items")
        sizePolicy1.setHeightForWidth(
            self.randomized_items.sizePolicy().hasHeightForWidth()
        )
        self.randomized_items.setSizePolicy(sizePolicy1)
        self.randomized_items.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.randomized_items.setProperty("showDropIndicator", False)
        self.randomized_items.setSelectionMode(QAbstractItemView.MultiSelection)
        self.randomized_items.setSelectionRectVisible(False)

        self.vlay_randomized_items_section.addWidget(self.randomized_items)

        self.horizontalLayout_5.addLayout(self.vlay_randomized_items_section)

        self.vlay_starting_items_controls = QVBoxLayout()
        self.vlay_starting_items_controls.setObjectName("vlay_starting_items_controls")
        self.vlay_starting_items_controls.setSizeConstraint(
            QLayout.SetDefaultConstraint
        )
        self.vspace_starting_items_controls_upper = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_starting_items_controls.addItem(
            self.vspace_starting_items_controls_upper
        )

        self.randomize_item = QPushButton(self.box_starting_items)
        self.randomize_item.setObjectName("randomize_item")
        sizePolicy7.setHeightForWidth(
            self.randomize_item.sizePolicy().hasHeightForWidth()
        )
        self.randomize_item.setSizePolicy(sizePolicy7)

        self.vlay_starting_items_controls.addWidget(self.randomize_item)

        self.vspace_starting_items_controls_middle = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_starting_items_controls.addItem(
            self.vspace_starting_items_controls_middle
        )

        self.start_with_item = QPushButton(self.box_starting_items)
        self.start_with_item.setObjectName("start_with_item")
        sizePolicy7.setHeightForWidth(
            self.start_with_item.sizePolicy().hasHeightForWidth()
        )
        self.start_with_item.setSizePolicy(sizePolicy7)

        self.vlay_starting_items_controls.addWidget(self.start_with_item)

        self.vspace_starting_items_controls_lower = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_starting_items_controls.addItem(
            self.vspace_starting_items_controls_lower
        )

        self.horizontalLayout_5.addLayout(self.vlay_starting_items_controls)

        self.vlay_starting_items_section = QVBoxLayout()
        self.vlay_starting_items_section.setObjectName("vlay_starting_items_section")
        self.label_starting_items = QLabel(self.box_starting_items)
        self.label_starting_items.setObjectName("label_starting_items")

        self.vlay_starting_items_section.addWidget(self.label_starting_items)

        self.starting_items_free_search = QLineEdit(self.box_starting_items)
        self.starting_items_free_search.setObjectName("starting_items_free_search")
        self.starting_items_free_search.setClearButtonEnabled(True)

        self.vlay_starting_items_section.addWidget(self.starting_items_free_search)

        self.starting_items = QListView(self.box_starting_items)
        self.starting_items.setObjectName("starting_items")
        sizePolicy1.setHeightForWidth(
            self.starting_items.sizePolicy().hasHeightForWidth()
        )
        self.starting_items.setSizePolicy(sizePolicy1)
        self.starting_items.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.starting_items.setProperty("showDropIndicator", False)
        self.starting_items.setSelectionMode(QAbstractItemView.MultiSelection)
        self.starting_items.setSelectionRectVisible(False)

        self.vlay_starting_items_section.addWidget(self.starting_items)

        self.horizontalLayout_5.addLayout(self.vlay_starting_items_section)

        self.horizontalLayout_8.addWidget(self.box_starting_items)

        self.box_additional_options = QGroupBox(self.tab_starting_items)
        self.box_additional_options.setObjectName("box_additional_options")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(
            self.box_additional_options.sizePolicy().hasHeightForWidth()
        )
        self.box_additional_options.setSizePolicy(sizePolicy8)
        self.verticalLayout_29 = QVBoxLayout(self.box_additional_options)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_for_option_starting_sword = QLabel(self.box_additional_options)
        self.label_for_option_starting_sword.setObjectName(
            "label_for_option_starting_sword"
        )

        self.verticalLayout_29.addWidget(self.label_for_option_starting_sword)

        self.option_starting_sword = QComboBox(self.box_additional_options)
        self.option_starting_sword.setObjectName("option_starting_sword")

        self.verticalLayout_29.addWidget(self.option_starting_sword)

        self.hlay_starting_tablets = QHBoxLayout()
        self.hlay_starting_tablets.setObjectName("hlay_starting_tablets")
        self.label_for_option_starting_tablet_count = QLabel(
            self.box_additional_options
        )
        self.label_for_option_starting_tablet_count.setObjectName(
            "label_for_option_starting_tablet_count"
        )

        self.hlay_starting_tablets.addWidget(
            self.label_for_option_starting_tablet_count
        )

        self.option_starting_tablet_count = QSpinBox(self.box_additional_options)
        self.option_starting_tablet_count.setObjectName("option_starting_tablet_count")
        sizePolicy5.setHeightForWidth(
            self.option_starting_tablet_count.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_tablet_count.setSizePolicy(sizePolicy5)
        self.option_starting_tablet_count.setMaximumSize(QSize(16777215, 16777215))

        self.hlay_starting_tablets.addWidget(self.option_starting_tablet_count)

        self.verticalLayout_29.addLayout(self.hlay_starting_tablets)

        self.hlay_starting_bottles = QHBoxLayout()
        self.hlay_starting_bottles.setObjectName("hlay_starting_bottles")
        self.label_for_option_starting_bottles = QLabel(self.box_additional_options)
        self.label_for_option_starting_bottles.setObjectName(
            "label_for_option_starting_bottles"
        )

        self.hlay_starting_bottles.addWidget(self.label_for_option_starting_bottles)

        self.option_starting_bottles = QSpinBox(self.box_additional_options)
        self.option_starting_bottles.setObjectName("option_starting_bottles")
        sizePolicy5.setHeightForWidth(
            self.option_starting_bottles.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_bottles.setSizePolicy(sizePolicy5)

        self.hlay_starting_bottles.addWidget(self.option_starting_bottles)

        self.verticalLayout_29.addLayout(self.hlay_starting_bottles)

        self.hlay_starting_crystal_packs = QHBoxLayout()
        self.hlay_starting_crystal_packs.setObjectName("hlay_starting_crystal_packs")
        self.label_for_option_starting_crystal_packs = QLabel(
            self.box_additional_options
        )
        self.label_for_option_starting_crystal_packs.setObjectName(
            "label_for_option_starting_crystal_packs"
        )

        self.hlay_starting_crystal_packs.addWidget(
            self.label_for_option_starting_crystal_packs
        )

        self.option_starting_crystal_packs = QSpinBox(self.box_additional_options)
        self.option_starting_crystal_packs.setObjectName(
            "option_starting_crystal_packs"
        )
        sizePolicy5.setHeightForWidth(
            self.option_starting_crystal_packs.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_crystal_packs.setSizePolicy(sizePolicy5)

        self.hlay_starting_crystal_packs.addWidget(self.option_starting_crystal_packs)

        self.verticalLayout_29.addLayout(self.hlay_starting_crystal_packs)

        self.hlay_starting_tadtones = QHBoxLayout()
        self.hlay_starting_tadtones.setObjectName("hlay_starting_tadtones")
        self.hlay_starting_tadtones.setContentsMargins(-1, 0, -1, -1)
        self.label_for_option_starting_tadtones = QLabel(self.box_additional_options)
        self.label_for_option_starting_tadtones.setObjectName(
            "label_for_option_starting_tadtones"
        )

        self.hlay_starting_tadtones.addWidget(self.label_for_option_starting_tadtones)

        self.option_starting_tadtones = QSpinBox(self.box_additional_options)
        self.option_starting_tadtones.setObjectName("option_starting_tadtones")
        sizePolicy5.setHeightForWidth(
            self.option_starting_tadtones.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_tadtones.setSizePolicy(sizePolicy5)

        self.hlay_starting_tadtones.addWidget(self.option_starting_tadtones)

        self.verticalLayout_29.addLayout(self.hlay_starting_tadtones)

        self.option_random_starting_item = QCheckBox(self.box_additional_options)
        self.option_random_starting_item.setObjectName("option_random_starting_item")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.option_random_starting_item.sizePolicy().hasHeightForWidth()
        )
        self.option_random_starting_item.setSizePolicy(sizePolicy9)

        self.verticalLayout_29.addWidget(self.option_random_starting_item)

        self.option_start_with_hylian_shield = QCheckBox(self.box_additional_options)
        self.option_start_with_hylian_shield.setObjectName(
            "option_start_with_hylian_shield"
        )

        self.verticalLayout_29.addWidget(self.option_start_with_hylian_shield)

        self.option_full_starting_wallet = QCheckBox(self.box_additional_options)
        self.option_full_starting_wallet.setObjectName("option_full_starting_wallet")

        self.verticalLayout_29.addWidget(self.option_full_starting_wallet)

        self.option_max_starting_bugs = QCheckBox(self.box_additional_options)
        self.option_max_starting_bugs.setObjectName("option_max_starting_bugs")

        self.verticalLayout_29.addWidget(self.option_max_starting_bugs)

        self.option_max_starting_treasures = QCheckBox(self.box_additional_options)
        self.option_max_starting_treasures.setObjectName(
            "option_max_starting_treasures"
        )

        self.verticalLayout_29.addWidget(self.option_max_starting_treasures)

        self.hlay_heart_options = QHBoxLayout()
        self.hlay_heart_options.setObjectName("hlay_heart_options")
        self.label_for_option_starting_heart_containers = QLabel(
            self.box_additional_options
        )
        self.label_for_option_starting_heart_containers.setObjectName(
            "label_for_option_starting_heart_containers"
        )
        sizePolicy6.setHeightForWidth(
            self.label_for_option_starting_heart_containers.sizePolicy().hasHeightForWidth()
        )
        self.label_for_option_starting_heart_containers.setSizePolicy(sizePolicy6)

        self.hlay_heart_options.addWidget(
            self.label_for_option_starting_heart_containers
        )

        self.option_starting_heart_containers = QSpinBox(self.box_additional_options)
        self.option_starting_heart_containers.setObjectName(
            "option_starting_heart_containers"
        )
        sizePolicy9.setHeightForWidth(
            self.option_starting_heart_containers.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_heart_containers.setSizePolicy(sizePolicy9)
        self.option_starting_heart_containers.setMaximumSize(QSize(41, 16777215))

        self.hlay_heart_options.addWidget(self.option_starting_heart_containers)

        self.label_for_option_starting_heart_pieces = QLabel(
            self.box_additional_options
        )
        self.label_for_option_starting_heart_pieces.setObjectName(
            "label_for_option_starting_heart_pieces"
        )
        sizePolicy6.setHeightForWidth(
            self.label_for_option_starting_heart_pieces.sizePolicy().hasHeightForWidth()
        )
        self.label_for_option_starting_heart_pieces.setSizePolicy(sizePolicy6)

        self.hlay_heart_options.addWidget(self.label_for_option_starting_heart_pieces)

        self.option_starting_heart_pieces = QSpinBox(self.box_additional_options)
        self.option_starting_heart_pieces.setObjectName("option_starting_heart_pieces")
        sizePolicy9.setHeightForWidth(
            self.option_starting_heart_pieces.sizePolicy().hasHeightForWidth()
        )
        self.option_starting_heart_pieces.setSizePolicy(sizePolicy9)
        self.option_starting_heart_pieces.setMaximumSize(QSize(41, 16777215))

        self.hlay_heart_options.addWidget(self.option_starting_heart_pieces)

        self.verticalLayout_29.addLayout(self.hlay_heart_options)

        self.hlay_heart_display = QHBoxLayout()
        self.hlay_heart_display.setObjectName("hlay_heart_display")
        self.label_current_starting_health = QLabel(self.box_additional_options)
        self.label_current_starting_health.setObjectName(
            "label_current_starting_health"
        )

        self.hlay_heart_display.addWidget(self.label_current_starting_health)

        self.current_starting_health_counter = QLabel(self.box_additional_options)
        self.current_starting_health_counter.setObjectName(
            "current_starting_health_counter"
        )
        sizePolicy2.setHeightForWidth(
            self.current_starting_health_counter.sizePolicy().hasHeightForWidth()
        )
        self.current_starting_health_counter.setSizePolicy(sizePolicy2)

        self.hlay_heart_display.addWidget(self.current_starting_health_counter)

        self.verticalLayout_29.addLayout(self.hlay_heart_display)

        self.vspace_additional_options = QSpacerItem(
            20, 137, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_29.addItem(self.vspace_additional_options)

        self.horizontalLayout_8.addWidget(self.box_additional_options)

        self.tabWidget.addTab(self.tab_starting_items, "")
        self.tab_cosmetics = QWidget()
        self.tab_cosmetics.setObjectName("tab_cosmetics")
        self.verticalLayout_31 = QVBoxLayout(self.tab_cosmetics)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.hlay_cosmetics = QHBoxLayout()
        self.hlay_cosmetics.setObjectName("hlay_cosmetics")
        self.hlay_cosmetics.setContentsMargins(-1, -1, -1, 0)
        self.custom_model_settings = QVBoxLayout()
        self.custom_model_settings.setObjectName("custom_model_settings")
        self.hlay_type_options = QHBoxLayout()
        self.hlay_type_options.setObjectName("hlay_type_options")
        self.label_color_preset_select_label = QLabel(self.tab_cosmetics)
        self.label_color_preset_select_label.setObjectName(
            "label_color_preset_select_label"
        )

        self.hlay_type_options.addWidget(self.label_color_preset_select_label)

        self.option_model_type_select = QComboBox(self.tab_cosmetics)
        self.option_model_type_select.setObjectName("option_model_type_select")
        self.option_model_type_select.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(20)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(
            self.option_model_type_select.sizePolicy().hasHeightForWidth()
        )
        self.option_model_type_select.setSizePolicy(sizePolicy10)

        self.hlay_type_options.addWidget(self.option_model_type_select)

        self.option_tunic_swap = QCheckBox(self.tab_cosmetics)
        self.option_tunic_swap.setObjectName("option_tunic_swap")
        self.option_tunic_swap.setEnabled(True)
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(40)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(
            self.option_tunic_swap.sizePolicy().hasHeightForWidth()
        )
        self.option_tunic_swap.setSizePolicy(sizePolicy11)

        self.hlay_type_options.addWidget(self.option_tunic_swap)

        self.hspace_type_options = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.hlay_type_options.addItem(self.hspace_type_options)

        self.custom_model_settings.addLayout(self.hlay_type_options)

        self.hlay_pack_options = QHBoxLayout()
        self.hlay_pack_options.setObjectName("hlay_pack_options")
        self.label_player_model_select = QLabel(self.tab_cosmetics)
        self.label_player_model_select.setObjectName("label_player_model_select")

        self.hlay_pack_options.addWidget(self.label_player_model_select)

        self.option_model_pack_select = QComboBox(self.tab_cosmetics)
        self.option_model_pack_select.setObjectName("option_model_pack_select")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(20)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(
            self.option_model_pack_select.sizePolicy().hasHeightForWidth()
        )
        self.option_model_pack_select.setSizePolicy(sizePolicy12)

        self.hlay_pack_options.addWidget(self.option_model_pack_select)

        self.button_randomize_all_colors = QPushButton(self.tab_cosmetics)
        self.button_randomize_all_colors.setObjectName("button_randomize_all_colors")
        sizePolicy12.setHeightForWidth(
            self.button_randomize_all_colors.sizePolicy().hasHeightForWidth()
        )
        self.button_randomize_all_colors.setSizePolicy(sizePolicy12)

        self.hlay_pack_options.addWidget(self.button_randomize_all_colors)

        self.button_reset_all_colors = QPushButton(self.tab_cosmetics)
        self.button_reset_all_colors.setObjectName("button_reset_all_colors")
        sizePolicy12.setHeightForWidth(
            self.button_reset_all_colors.sizePolicy().hasHeightForWidth()
        )
        self.button_reset_all_colors.setSizePolicy(sizePolicy12)

        self.hlay_pack_options.addWidget(self.button_reset_all_colors)

        self.hspace_pack_options = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.hlay_pack_options.addItem(self.hspace_pack_options)

        self.custom_model_settings.addLayout(self.hlay_pack_options)

        self.hlay_cosmetics.addLayout(self.custom_model_settings)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.button_save_color_preset = QPushButton(self.tab_cosmetics)
        self.button_save_color_preset.setObjectName("button_save_color_preset")

        self.gridLayout.addWidget(self.button_save_color_preset, 1, 2, 1, 1)

        self.button_load_color_preset = QPushButton(self.tab_cosmetics)
        self.button_load_color_preset.setObjectName("button_load_color_preset")

        self.gridLayout.addWidget(self.button_load_color_preset, 1, 1, 1, 1)

        self.button_delete_color_preset = QPushButton(self.tab_cosmetics)
        self.button_delete_color_preset.setObjectName("button_delete_color_preset")

        self.gridLayout.addWidget(self.button_delete_color_preset, 1, 3, 1, 1)

        self.button_color_imports = QPushButton(self.tab_cosmetics)
        self.button_color_imports.setObjectName("button_color_imports")

        self.gridLayout.addWidget(self.button_color_imports, 1, 0, 1, 1)

        self.label_for_color_presets = QLabel(self.tab_cosmetics)
        self.label_for_color_presets.setObjectName("label_for_color_presets")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(20)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(
            self.label_for_color_presets.sizePolicy().hasHeightForWidth()
        )
        self.label_for_color_presets.setSizePolicy(sizePolicy13)
        self.label_for_color_presets.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.label_for_color_presets, 0, 0, 1, 1)

        self.color_presets_list = QComboBox(self.tab_cosmetics)
        self.color_presets_list.setObjectName("color_presets_list")
        sizePolicy10.setHeightForWidth(
            self.color_presets_list.sizePolicy().hasHeightForWidth()
        )
        self.color_presets_list.setSizePolicy(sizePolicy10)

        self.gridLayout.addWidget(self.color_presets_list, 0, 1, 1, 3)

        self.hlay_cosmetics.addLayout(self.gridLayout)

        self.verticalLayout_31.addLayout(self.hlay_cosmetics)

        self.hlay_colors_and_preview = QHBoxLayout()
        self.hlay_colors_and_preview.setObjectName("hlay_colors_and_preview")
        self.scroll_area_colors = QScrollArea(self.tab_cosmetics)
        self.scroll_area_colors.setObjectName("scroll_area_colors")
        self.scroll_area_colors.setContextMenuPolicy(Qt.PreventContextMenu)
        self.scroll_area_colors.setFrameShape(QFrame.NoFrame)
        self.scroll_area_colors.setFrameShadow(QFrame.Plain)
        self.scroll_area_colors.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_colors.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_colors.setWidgetResizable(True)
        self.scroll_area_colors.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.scroll_area_widget_contents_colors = QWidget()
        self.scroll_area_widget_contents_colors.setObjectName(
            "scroll_area_widget_contents_colors"
        )
        self.scroll_area_widget_contents_colors.setGeometry(QRect(0, 0, 577, 477))
        self.verticalLayout_34 = QVBoxLayout(self.scroll_area_widget_contents_colors)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.vlay_texture_colors = QVBoxLayout()
        self.vlay_texture_colors.setObjectName("vlay_texture_colors")
        self.vspace_colors = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_texture_colors.addItem(self.vspace_colors)

        self.hspace_colors = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.vlay_texture_colors.addItem(self.hspace_colors)

        self.verticalLayout_34.addLayout(self.vlay_texture_colors)

        self.scroll_area_colors.setWidget(self.scroll_area_widget_contents_colors)

        self.hlay_colors_and_preview.addWidget(self.scroll_area_colors)

        self.vlay_preview = QVBoxLayout()
        self.vlay_preview.setObjectName("vlay_preview")
        self.hlay_preview = QHBoxLayout()
        self.hlay_preview.setObjectName("hlay_preview")
        self.label_preview_image = QLabel(self.tab_cosmetics)
        self.label_preview_image.setObjectName("label_preview_image")
        sizePolicy1.setHeightForWidth(
            self.label_preview_image.sizePolicy().hasHeightForWidth()
        )
        self.label_preview_image.setSizePolicy(sizePolicy1)
        self.label_preview_image.setScaledContents(False)
        self.label_preview_image.setAlignment(Qt.AlignCenter)

        self.hlay_preview.addWidget(self.label_preview_image)

        self.vlay_preview.addLayout(self.hlay_preview)

        self.hlay_colors_and_preview.addLayout(self.vlay_preview)

        self.verticalLayout_31.addLayout(self.hlay_colors_and_preview)

        self.tabWidget.addTab(self.tab_cosmetics, "")
        self.tab_accessibility = QWidget()
        self.tab_accessibility.setObjectName("tab_accessibility")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_accessibility)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.box_theme = QGroupBox(self.tab_accessibility)
        self.box_theme.setObjectName("box_theme")
        sizePolicy2.setHeightForWidth(self.box_theme.sizePolicy().hasHeightForWidth())
        self.box_theme.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.box_theme)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vlay_theme = QVBoxLayout()
        self.vlay_theme.setObjectName("vlay_theme")
        self.theme_mode_label = QLabel(self.box_theme)
        self.theme_mode_label.setObjectName("theme_mode_label")

        self.vlay_theme.addWidget(self.theme_mode_label)

        self.option_theme_mode = QComboBox(self.box_theme)
        self.option_theme_mode.setObjectName("option_theme_mode")

        self.vlay_theme.addWidget(self.option_theme_mode)

        self.theme_presets_label = QLabel(self.box_theme)
        self.theme_presets_label.setObjectName("theme_presets_label")

        self.vlay_theme.addWidget(self.theme_presets_label)

        self.option_theme_presets = QComboBox(self.box_theme)
        self.option_theme_presets.setObjectName("option_theme_presets")

        self.vlay_theme.addWidget(self.option_theme_presets)

        self.option_use_custom_theme = QCheckBox(self.box_theme)
        self.option_use_custom_theme.setObjectName("option_use_custom_theme")

        self.vlay_theme.addWidget(self.option_use_custom_theme)

        self.custom_theme_button = QPushButton(self.box_theme)
        self.custom_theme_button.setObjectName("custom_theme_button")
        self.custom_theme_button.setEnabled(False)

        self.vlay_theme.addWidget(self.custom_theme_button)

        self.option_use_sharp_corners = QCheckBox(self.box_theme)
        self.option_use_sharp_corners.setObjectName("option_use_sharp_corners")

        self.vlay_theme.addWidget(self.option_use_sharp_corners)

        self.vspace_theme = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_theme.addItem(self.vspace_theme)

        self.verticalLayout_3.addLayout(self.vlay_theme)

        self.horizontalLayout_3.addWidget(self.box_theme)

        self.box_font = QGroupBox(self.tab_accessibility)
        self.box_font.setObjectName("box_font")
        sizePolicy2.setHeightForWidth(self.box_font.sizePolicy().hasHeightForWidth())
        self.box_font.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.box_font)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vlay_font = QVBoxLayout()
        self.vlay_font.setObjectName("vlay_font")
        self.label_for_option_font_family = QLabel(self.box_font)
        self.label_for_option_font_family.setObjectName("label_for_option_font_family")
        self.label_for_option_font_family.setFont(font)

        self.vlay_font.addWidget(self.label_for_option_font_family)

        self.option_font_family = QFontComboBox(self.box_font)
        self.option_font_family.setObjectName("option_font_family")
        sizePolicy14 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(
            self.option_font_family.sizePolicy().hasHeightForWidth()
        )
        self.option_font_family.setSizePolicy(sizePolicy14)
        self.option_font_family.setEditable(False)
        self.option_font_family.setSizeAdjustPolicy(
            QComboBox.AdjustToContentsOnFirstShow
        )
        self.option_font_family.setWritingSystem(QFontDatabase.Any)
        self.option_font_family.setFontFilters(QFontComboBox.ScalableFonts)
        font1 = QFont()
        font1.setFamilies(["Arial"])
        font1.setPointSize(10)
        self.option_font_family.setCurrentFont(font1)

        self.vlay_font.addWidget(self.option_font_family)

        self.hlay_font_size = QHBoxLayout()
        self.hlay_font_size.setObjectName("hlay_font_size")
        self.label_for_option_font_size = QLabel(self.box_font)
        self.label_for_option_font_size.setObjectName("label_for_option_font_size")
        sizePolicy.setHeightForWidth(
            self.label_for_option_font_size.sizePolicy().hasHeightForWidth()
        )
        self.label_for_option_font_size.setSizePolicy(sizePolicy)

        self.hlay_font_size.addWidget(self.label_for_option_font_size)

        self.option_font_size = QSpinBox(self.box_font)
        self.option_font_size.setObjectName("option_font_size")
        sizePolicy9.setHeightForWidth(
            self.option_font_size.sizePolicy().hasHeightForWidth()
        )
        self.option_font_size.setSizePolicy(sizePolicy9)

        self.hlay_font_size.addWidget(self.option_font_size)

        self.vlay_font.addLayout(self.hlay_font_size)

        self.reset_font_button = QPushButton(self.box_font)
        self.reset_font_button.setObjectName("reset_font_button")
        sizePolicy9.setHeightForWidth(
            self.reset_font_button.sizePolicy().hasHeightForWidth()
        )
        self.reset_font_button.setSizePolicy(sizePolicy9)

        self.vlay_font.addWidget(self.reset_font_button)

        self.vspace_font = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.vlay_font.addItem(self.vspace_font)

        self.verticalLayout_2.addLayout(self.vlay_font)

        self.horizontalLayout_3.addWidget(self.box_font)

        self.box_1 = QGroupBox(self.tab_accessibility)
        self.box_1.setObjectName("box_1")
        self.box_1.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.box_1.sizePolicy().hasHeightForWidth())
        self.box_1.setSizePolicy(sizePolicy2)
        self.box_1.setFlat(False)
        self.verticalLayout_9 = QVBoxLayout(self.box_1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.vspace = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.vspace)

        self.horizontalLayout_3.addWidget(self.box_1)

        self.box_2 = QGroupBox(self.tab_accessibility)
        self.box_2.setObjectName("box_2")
        self.box_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.box_2.sizePolicy().hasHeightForWidth())
        self.box_2.setSizePolicy(sizePolicy2)
        self.box_2.setFlat(False)
        self.verticalLayout_10 = QVBoxLayout(self.box_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vspace_2 = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.vspace_2)

        self.horizontalLayout_3.addWidget(self.box_2)

        self.box_3 = QGroupBox(self.tab_accessibility)
        self.box_3.setObjectName("box_3")
        self.box_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.box_3.sizePolicy().hasHeightForWidth())
        self.box_3.setSizePolicy(sizePolicy2)
        self.box_3.setFlat(False)
        self.verticalLayout_11 = QVBoxLayout(self.box_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.vspace_3 = QSpacerItem(20, 533, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.vspace_3)

        self.horizontalLayout_3.addWidget(self.box_3)

        self.tabWidget.addTab(self.tab_accessibility, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.option_description = QLabel(self.centralwidget)
        self.option_description.setObjectName("option_description")
        self.option_description.setEnabled(True)
        sizePolicy15 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(
            self.option_description.sizePolicy().hasHeightForWidth()
        )
        self.option_description.setSizePolicy(sizePolicy15)
        self.option_description.setMinimumSize(QSize(0, 48))
        self.option_description.setStyleSheet("")
        self.option_description.setTextFormat(Qt.MarkdownText)
        self.option_description.setWordWrap(True)

        self.verticalLayout.addWidget(self.option_description)

        self.vlay_bottom_controls = QVBoxLayout()
        self.vlay_bottom_controls.setObjectName("vlay_bottom_controls")
        self.hlay_permalink = QHBoxLayout()
        self.hlay_permalink.setObjectName("hlay_permalink")
        self.label_permalink = QLabel(self.centralwidget)
        self.label_permalink.setObjectName("label_permalink")

        self.hlay_permalink.addWidget(self.label_permalink)

        self.permalink = QLineEdit(self.centralwidget)
        self.permalink.setObjectName("permalink")

        self.hlay_permalink.addWidget(self.permalink)

        self.copy_permalink_button = QPushButton(self.centralwidget)
        self.copy_permalink_button.setObjectName("copy_permalink_button")

        self.hlay_permalink.addWidget(self.copy_permalink_button)

        self.vlay_bottom_controls.addLayout(self.hlay_permalink)

        self.hlay_seed = QHBoxLayout()
        self.hlay_seed.setObjectName("hlay_seed")
        self.label_seed = QLabel(self.centralwidget)
        self.label_seed.setObjectName("label_seed")
        self.label_seed.setToolTipDuration(-1)
        self.label_seed.setLayoutDirection(Qt.LeftToRight)
        self.label_seed.setAutoFillBackground(False)
        self.label_seed.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.hlay_seed.addWidget(self.label_seed)

        self.seed = QLineEdit(self.centralwidget)
        self.seed.setObjectName("seed")

        self.hlay_seed.addWidget(self.seed)

        self.seed_button = QPushButton(self.centralwidget)
        self.seed_button.setObjectName("seed_button")

        self.hlay_seed.addWidget(self.seed_button)

        self.vlay_bottom_controls.addLayout(self.hlay_seed)

        self.hlay_button_row = QHBoxLayout()
        self.hlay_button_row.setObjectName("hlay_button_row")
        self.randomize_button = QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")

        self.hlay_button_row.addWidget(self.randomize_button)

        self.vlay_bottom_controls.addLayout(self.hlay_button_row)

        self.verticalLayout.addLayout(self.vlay_bottom_controls)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(6)
        self.option_triforce_shuffle.setCurrentIndex(-1)
        self.option_randomize_entrances.setCurrentIndex(-1)
        self.option_chest_dowsing.setCurrentIndex(-1)
        self.option_model_pack_select.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Skyward Sword Randomizer", None)
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.label_output.setText(
            QCoreApplication.translate("MainWindow", "Output Folder", None)
        )
        self.ouput_folder_browse_button.setText(
            QCoreApplication.translate("MainWindow", "Browse", None)
        )
        self.option_plando.setText(
            QCoreApplication.translate("MainWindow", "Enable Plandomizer", None)
        )
        self.plando_file_browse.setText(
            QCoreApplication.translate("MainWindow", "Browse", None)
        )
        self.box_additional_files.setTitle(
            QCoreApplication.translate("MainWindow", "Additional File Generation", None)
        )
        self.option_no_spoiler_log.setText(
            QCoreApplication.translate("MainWindow", "No Spoiler Log", None)
        )
        self.option_json_spoiler.setText(
            QCoreApplication.translate("MainWindow", "Generate JSON Spoiler Log", None)
        )
        self.option_out_placement_file.setText(
            QCoreApplication.translate("MainWindow", "Generate Placement File", None)
        )
        self.box_advanced.setTitle(
            QCoreApplication.translate("MainWindow", "Advanced Options", None)
        )
        self.option_dry_run.setText(
            QCoreApplication.translate("MainWindow", "Dry Run", None)
        )
        self.box_cosmetics.setTitle(
            QCoreApplication.translate("MainWindow", "Cosmetics", None)
        )
        self.option_cryptic_location_hints.setText(
            QCoreApplication.translate("MainWindow", "Cryptic Location Hints", None)
        )
        self.option_lightning_skyward_strike.setText(
            QCoreApplication.translate("MainWindow", "Lightning Skyward Strike", None)
        )
        self.option_starry_skies.setText(
            QCoreApplication.translate("MainWindow", "Starry Skies", None)
        )
        self.label_for_option_star_count.setText(
            QCoreApplication.translate("MainWindow", "Number of stars", None)
        )
        self.label_for_option_interface.setText(
            QCoreApplication.translate("MainWindow", "Starting Interface", None)
        )
        self.box_music_rando.setTitle(
            QCoreApplication.translate("MainWindow", "Randomize Music", None)
        )
        self.label_for_option_music_rando.setText(
            QCoreApplication.translate("MainWindow", "Randomize Music", None)
        )
        self.option_cutoff_gameover_music.setText(
            QCoreApplication.translate("MainWindow", "Cutoff Game Over Music", None)
        )
        self.option_allow_custom_music.setText(
            QCoreApplication.translate("MainWindow", "Allow Custom Music", None)
        )
        self.option_no_enemy_music.setText(
            QCoreApplication.translate("MainWindow", "Remove Enemy Music", None)
        )
        self.box.setTitle("")
        self.box_presets.setTitle(
            QCoreApplication.translate("MainWindow", "Presets", None)
        )
        self.label_presets.setText(
            QCoreApplication.translate(
                "MainWindow", "Presets overwrite ALL game settings", None
            )
        )
        self.load_preset.setText(QCoreApplication.translate("MainWindow", "Load", None))
        self.save_preset.setText(QCoreApplication.translate("MainWindow", "Save", None))
        self.delete_preset.setText(
            QCoreApplication.translate("MainWindow", "Delete", None)
        )
        self.box_rs.setTitle(
            QCoreApplication.translate("MainWindow", "Random Settings", None)
        )
        self.option_random_settings.setText(
            QCoreApplication.translate("MainWindow", "Randomize Game Settings", None)
        )
        self.option_random_cosmetics.setText(
            QCoreApplication.translate(
                "MainWindow", "Randomize Cosmetic Settings", None
            )
        )
        self.label_random_settings_weighting.setText(
            QCoreApplication.translate("MainWindow", "Random Settings Weighting", None)
        )
        self.label_progression_locations.setText(
            QCoreApplication.translate(
                "MainWindow", "Randomized Progression Locations", None
            )
        )
        self.edit_progression_groups.setText(
            QCoreApplication.translate("MainWindow", "Edit Progression Locations", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_setup),
            QCoreApplication.translate("MainWindow", "Setup", None),
        )
        # if QT_CONFIG(tooltip)
        self.tab_randomization_settings.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.box_completion.setTitle(
            QCoreApplication.translate("MainWindow", "Completion Conditions", None)
        )
        self.label_for_option_got_starting_state.setText(
            QCoreApplication.translate("MainWindow", "Starting State", None)
        )
        self.label_for_option_got_sword_requirement.setText(
            QCoreApplication.translate("MainWindow", "Sword Requirement", None)
        )
        self.label_for_option_got_dungeon_requirement.setText(
            QCoreApplication.translate("MainWindow", "Dungeon Requirement", None)
        )
        self.label_for_option_required_dungeon_count.setText(
            QCoreApplication.translate("MainWindow", "Required Dungeons", None)
        )
        self.option_triforce_required.setText(
            QCoreApplication.translate("MainWindow", "Triforce Required", None)
        )
        self.label_for_option_triforce_shuffle.setText(
            QCoreApplication.translate("MainWindow", "Triforce Shuffle", None)
        )
        self.option_triforce_shuffle.setCurrentText("")
        self.option_imp_2.setText(
            QCoreApplication.translate("MainWindow", "Skip Imprisoned 2", None)
        )
        self.option_horde.setText(
            QCoreApplication.translate("MainWindow", "Skip Horde", None)
        )
        self.option_g3.setText(
            QCoreApplication.translate("MainWindow", "Skip Ghirahim 3", None)
        )
        self.option_demise.setText(
            QCoreApplication.translate("MainWindow", "Skip Demise", None)
        )
        self.label_for_option_demise_count.setText(
            QCoreApplication.translate("MainWindow", "Demise Count", None)
        )
        self.box_open.setTitle(
            QCoreApplication.translate("MainWindow", "Open Settings", None)
        )
        self.label_for_option_open_thunderhead.setText(
            QCoreApplication.translate("MainWindow", "Open Thunderhead", None)
        )
        self.option_open_et.setText(
            QCoreApplication.translate("MainWindow", "Open Earth Temple", None)
        )
        self.label_for_option_open_lmf.setText(
            QCoreApplication.translate(
                "MainWindow", "Open Lanayru Mining Facility", None
            )
        )
        self.label_for_option_open_lake_floria.setText(
            QCoreApplication.translate("MainWindow", "Open Lake Floria", None)
        )
        self.option_random_puzzles.setText(
            QCoreApplication.translate("MainWindow", "Randomize Puzzles", None)
        )
        self.box_shuffles.setTitle(
            QCoreApplication.translate("MainWindow", "Shuffles", None)
        )
        self.label_for_option_batreaux_counts.setText(
            QCoreApplication.translate("MainWindow", "Batreaux Crystal Counts", None)
        )
        self.option_shopsanity.setText(
            QCoreApplication.translate("MainWindow", "Shuffle Beedle's Shop", None)
        )
        self.option_rupeesanity.setText(
            QCoreApplication.translate("MainWindow", "Rupeesanity", None)
        )
        self.option_tadtonesanity.setText(
            QCoreApplication.translate("MainWindow", "Tadtonesanity", None)
        )
        self.box_entrance_rando.setTitle(
            QCoreApplication.translate("MainWindow", "Entrance Randomization", None)
        )
        self.label_for_option_randomize_entrances.setText(
            QCoreApplication.translate(
                "MainWindow", "Randomize Dungeon Entrances", None
            )
        )
        self.option_randomize_entrances.setCurrentText("")
        self.option_randomize_trials.setText(
            QCoreApplication.translate(
                "MainWindow", "Randomize Silent Realm Gates", None
            )
        )
        self.label_for_option_random_start_entrance.setText(
            QCoreApplication.translate("MainWindow", "Randomize Starting Spawn", None)
        )
        self.option_limit_start_entrance.setText(
            QCoreApplication.translate("MainWindow", "Limit Starting Location", None)
        )
        self.option_random_start_statues.setText(
            QCoreApplication.translate("MainWindow", "Randomize Starting Statues", None)
        )
        self.box_dungeons.setTitle(
            QCoreApplication.translate("MainWindow", "Dungeons", None)
        )
        self.label_for_option_map_mode.setText(
            QCoreApplication.translate("MainWindow", "Map Mode", None)
        )
        self.label_for_option_small_key_mode.setText(
            QCoreApplication.translate("MainWindow", "Small Keys", None)
        )
        self.label_for_option_boss_key_mode.setText(
            QCoreApplication.translate("MainWindow", "Boss Keys", None)
        )
        self.option_empty_unrequired_dungeons.setText(
            QCoreApplication.translate("MainWindow", "Empty Unrequired Dungeons", None)
        )
        self.label_for_sword_dungeon_reward.setText(
            QCoreApplication.translate("MainWindow", "Sword Dungeon Reward", None)
        )
        self.option_randomize_boss_key_puzzles.setText(
            QCoreApplication.translate("MainWindow", "Randomize Boss Key Puzzles", None)
        )
        self.label_for_dungeon_patches.setText(
            QCoreApplication.translate(
                "MainWindow", "Dungeon Convenience Patches", None
            )
        )
        self.option_fs_lava_flow.setText(
            QCoreApplication.translate(
                "MainWindow", "Skip Fire Sanctuary Lava Chase", None
            )
        )
        self.label_for_dungeon_shortcuts.setText(
            QCoreApplication.translate("MainWindow", "Open Dungeon Shortcuts", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_randomization_settings),
            QCoreApplication.translate("MainWindow", "Randomization Settings", None),
        )
        self.box_convenience_tweaks.setTitle(
            QCoreApplication.translate("MainWindow", "Convenience Tweaks", None)
        )
        self.option_fill_dowsing_on_white_sword.setText(
            QCoreApplication.translate(
                "MainWindow", "Fill Dowsing on White Sword", None
            )
        )
        self.option_full_wallet_upgrades.setText(
            QCoreApplication.translate("MainWindow", "Full Wallet Upgrades", None)
        )
        self.box_vanilla_tweaks.setTitle(
            QCoreApplication.translate("MainWindow", "Vanilla Tweaks", None)
        )
        self.label_for_option_bit_patches.setText(
            QCoreApplication.translate("MainWindow", "BiT Patches", None)
        )
        self.label_for_option_peatrice_conversations.setText(
            QCoreApplication.translate("MainWindow", "Peatrice Conversations", None)
        )
        self.box_item_pool.setTitle(
            QCoreApplication.translate("MainWindow", "Item Pool", None)
        )
        self.option_gondo_upgrades.setText(
            QCoreApplication.translate("MainWindow", "Place Scrap Shop Upgrades", None)
        )
        self.label_for_option_rupoor_mode.setText(
            QCoreApplication.translate("MainWindow", "Rupoor Mode", None)
        )
        self.box_silent_realms.setTitle(
            QCoreApplication.translate("MainWindow", "Silent Realms", None)
        )
        self.label_for_option_shuffle_trial_objects.setText(
            QCoreApplication.translate("MainWindow", "Shuffle Trial Objects", None)
        )
        self.option_treasuresanity_in_silent_realms.setText(
            QCoreApplication.translate("MainWindow", "Trial Treasuresanity", None)
        )
        self.label_for_option_trial_treasure_amount.setText(
            QCoreApplication.translate("MainWindow", "Trial Treasure Amount", None)
        )
        self.box_heromode_changes.setTitle(
            QCoreApplication.translate("MainWindow", "Hero Mode Changes", None)
        )
        self.option_upgraded_skyward_strike.setText(
            QCoreApplication.translate("MainWindow", "Upgraded Skyward Strike", None)
        )
        self.option_fast_air_meter.setText(
            QCoreApplication.translate("MainWindow", "Faster Air Meter Depletion", None)
        )
        self.option_enable_heart_drops.setText(
            QCoreApplication.translate(
                "MainWindow", "Spawn Hearts and Heart Flowers", None
            )
        )
        self.label_for_option_damage_multiplier.setText(
            QCoreApplication.translate("MainWindow", "Damage Taken Multiplier", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_additional_settings),
            QCoreApplication.translate("MainWindow", "Additional Settings", None),
        )
        self.label_for_option_logic_mode.setText(
            QCoreApplication.translate("MainWindow", "Logic Mode", None)
        )
        self.edit_tricks.setText(
            QCoreApplication.translate("MainWindow", "Tricks", None)
        )
        self.label_include_locations.setText(
            QCoreApplication.translate("MainWindow", "Included Locations", None)
        )
        self.include_category_filters.setPlaceholderText("")
        self.included_free_search.setText("")
        self.included_free_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Search", None)
        )
        self.include_location.setText(
            QCoreApplication.translate("MainWindow", "Include\n" "<--", None)
        )
        self.exclude_location.setText(
            QCoreApplication.translate("MainWindow", "Exclude\n" "-->", None)
        )
        self.label_exclude_locations.setText(
            QCoreApplication.translate("MainWindow", "Excluded Locations", None)
        )
        self.excluded_free_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Search", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_logic_settings),
            QCoreApplication.translate("MainWindow", "Logic Settings", None),
        )
        self.box_stone_hints.setTitle(
            QCoreApplication.translate("MainWindow", "Gossip Stone Hints", None)
        )
        self.label_for_option_hint_distribution.setText(
            QCoreApplication.translate("MainWindow", "Hint Distribution", None)
        )
        self.option_cube_sots.setText(
            QCoreApplication.translate("MainWindow", "Separate Cube SotS Hints", None)
        )
        self.option_precise_item.setText(
            QCoreApplication.translate("MainWindow", "Precise Item Hints", None)
        )
        self.option_hint_importance.setText(
            QCoreApplication.translate("MainWindow", "Hint Importance", None)
        )
        self.box_other_hints.setTitle(
            QCoreApplication.translate("MainWindow", "Other Hints", None)
        )
        self.label_for_option_song_hints.setText(
            QCoreApplication.translate("MainWindow", "Song Hints", None)
        )
        self.option_impa_sot_hint.setText(
            QCoreApplication.translate("MainWindow", "Impa Stone of Trials Hint", None)
        )
        self.label_for_option_chest_dowsing.setText(
            QCoreApplication.translate("MainWindow", "Chest Dowsing", None)
        )
        self.option_chest_dowsing.setCurrentText("")
        self.option_dungeon_dowsing.setText(
            QCoreApplication.translate("MainWindow", "Allow Dowsing in Dungeons", None)
        )
        self.box_4.setTitle("")
        self.box_5.setTitle("")
        self.box_6.setTitle("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_hints),
            QCoreApplication.translate("MainWindow", "Hints", None),
        )
        self.box_starting_items.setTitle(
            QCoreApplication.translate("MainWindow", "Items", None)
        )
        self.label_randomized_items.setText(
            QCoreApplication.translate("MainWindow", "Randomized Items", None)
        )
        self.randomized_items_free_search.setText("")
        self.randomized_items_free_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Search", None)
        )
        self.randomize_item.setText(
            QCoreApplication.translate("MainWindow", "Remove\n" "<--", None)
        )
        self.start_with_item.setText(
            QCoreApplication.translate("MainWindow", "Add\n" "-->", None)
        )
        self.label_starting_items.setText(
            QCoreApplication.translate("MainWindow", "Starting Items", None)
        )
        self.starting_items_free_search.setText("")
        self.starting_items_free_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Search", None)
        )
        self.box_additional_options.setTitle(
            QCoreApplication.translate("MainWindow", "Additional Options", None)
        )
        self.label_for_option_starting_sword.setText(
            QCoreApplication.translate("MainWindow", "Starting Sword", None)
        )
        self.label_for_option_starting_tablet_count.setText(
            QCoreApplication.translate("MainWindow", "Starting Tablets", None)
        )
        self.label_for_option_starting_bottles.setText(
            QCoreApplication.translate("MainWindow", "Starting Empty Bottles", None)
        )
        self.label_for_option_starting_crystal_packs.setText(
            QCoreApplication.translate(
                "MainWindow", "Starting Gratitude Crystal Packs", None
            )
        )
        self.label_for_option_starting_tadtones.setText(
            QCoreApplication.translate(
                "MainWindow", "Starting Groups of Tadtones", None
            )
        )
        self.option_random_starting_item.setText(
            QCoreApplication.translate(
                "MainWindow", "Start with Random Progress Item", None
            )
        )
        self.option_start_with_hylian_shield.setText(
            QCoreApplication.translate("MainWindow", "Start with Hylian Shield", None)
        )
        self.option_full_starting_wallet.setText(
            QCoreApplication.translate("MainWindow", "Start with Full Wallet", None)
        )
        self.option_max_starting_bugs.setText(
            QCoreApplication.translate("MainWindow", "Maximum Starting Bugs", None)
        )
        self.option_max_starting_treasures.setText(
            QCoreApplication.translate("MainWindow", "Maximum Starting Treasures", None)
        )
        self.label_for_option_starting_heart_containers.setText(
            QCoreApplication.translate("MainWindow", "Heart Containers", None)
        )
        self.label_for_option_starting_heart_pieces.setText(
            QCoreApplication.translate("MainWindow", "Heart Pieces", None)
        )
        self.label_current_starting_health.setText(
            QCoreApplication.translate("MainWindow", "Starting Health:", None)
        )
        self.current_starting_health_counter.setText(
            QCoreApplication.translate("MainWindow", "6 hearts", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_starting_items),
            QCoreApplication.translate("MainWindow", "Starting Items", None),
        )
        self.label_color_preset_select_label.setText(
            QCoreApplication.translate("MainWindow", "Type", None)
        )
        self.option_tunic_swap.setText(
            QCoreApplication.translate("MainWindow", "Tunic Swap", None)
        )
        self.label_player_model_select.setText(
            QCoreApplication.translate("MainWindow", "Pack", None)
        )
        self.button_randomize_all_colors.setText(
            QCoreApplication.translate("MainWindow", "Randomize All Colors", None)
        )
        self.button_reset_all_colors.setText(
            QCoreApplication.translate("MainWindow", "Reset All Colors", None)
        )
        self.button_save_color_preset.setText(
            QCoreApplication.translate("MainWindow", "Save", None)
        )
        self.button_load_color_preset.setText(
            QCoreApplication.translate("MainWindow", "Load", None)
        )
        self.button_delete_color_preset.setText(
            QCoreApplication.translate("MainWindow", "Delete", None)
        )
        self.button_color_imports.setText(
            QCoreApplication.translate("MainWindow", "Import/Export", None)
        )
        self.label_for_color_presets.setText(
            QCoreApplication.translate("MainWindow", "Color Presets", None)
        )
        self.label_preview_image.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_cosmetics),
            QCoreApplication.translate("MainWindow", "Cosmetics", None),
        )
        self.box_theme.setTitle(
            QCoreApplication.translate("MainWindow", "Theming", None)
        )
        self.theme_mode_label.setText(
            QCoreApplication.translate("MainWindow", "Theme Mode", None)
        )
        self.option_theme_mode.setCurrentText("")
        self.theme_presets_label.setText(
            QCoreApplication.translate("MainWindow", "Theme Presets", None)
        )
        self.option_theme_presets.setCurrentText("")
        self.option_use_custom_theme.setText(
            QCoreApplication.translate("MainWindow", "Use Custom Theme", None)
        )
        self.custom_theme_button.setText(
            QCoreApplication.translate("MainWindow", "Customize Theme", None)
        )
        self.option_use_sharp_corners.setText(
            QCoreApplication.translate("MainWindow", "Sharp Corners", None)
        )
        self.box_font.setTitle(QCoreApplication.translate("MainWindow", "Fonts", None))
        self.label_for_option_font_family.setText(
            QCoreApplication.translate("MainWindow", "Font Family", None)
        )
        self.option_font_family.setCurrentText(
            QCoreApplication.translate("MainWindow", "Arial", None)
        )
        self.option_font_family.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Select Font Family", None)
        )
        self.label_for_option_font_size.setText(
            QCoreApplication.translate("MainWindow", "Font Size", None)
        )
        self.reset_font_button.setText(
            QCoreApplication.translate("MainWindow", "Reset", None)
        )
        self.box_1.setTitle("")
        self.box_2.setTitle("")
        self.box_3.setTitle("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_accessibility),
            QCoreApplication.translate("MainWindow", "Accessibility", None),
        )
        self.option_description.setText("")
        self.label_permalink.setText(
            QCoreApplication.translate("MainWindow", "Settings String", None)
        )
        self.copy_permalink_button.setText(
            QCoreApplication.translate("MainWindow", "Copy Settings String", None)
        )
        # if QT_CONFIG(tooltip)
        self.label_seed.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.label_seed.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.label_seed.setText(QCoreApplication.translate("MainWindow", "Seed", None))
        self.seed_button.setText(
            QCoreApplication.translate("MainWindow", "New Seed", None)
        )
        self.randomize_button.setText(
            QCoreApplication.translate("MainWindow", "Randomize", None)
        )

    # retranslateUi
