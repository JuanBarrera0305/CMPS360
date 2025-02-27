import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class NetflixMovieGUI {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(NetflixMovieGUI::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Netflix Movie Management");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setLayout(new BorderLayout());

        JPanel inputPanel = new JPanel(new GridLayout(13, 2, 5, 5));
        String[] labels = {"Title", "Genre", "Release Year", "Director", "Main Actor", "Main Actress", "Language", "Duration (min)", "IMDb Rating", "Viewer Restriction"};
        JTextField[] fields = new JTextField[labels.length];

        for (int i = 0; i < labels.length; i++) {
            inputPanel.add(new JLabel(labels[i] + ":"));
            fields[i] = new JTextField();
            inputPanel.add(fields[i]);
        }

        JComboBox<String> contentType = new JComboBox<>(new String[]{"Movie", "Series"});
        JTextField seasonsField = new JTextField();
        JTextField episodesField = new JTextField();

        inputPanel.add(new JLabel("Content Type:"));
        inputPanel.add(contentType);
        inputPanel.add(new JLabel("Seasons:"));
        inputPanel.add(seasonsField);
        inputPanel.add(new JLabel("Episodes:"));
        inputPanel.add(episodesField);

        seasonsField.setEnabled(false);
        episodesField.setEnabled(false);

        contentType.addActionListener(e -> {
            boolean isSeries = contentType.getSelectedItem().equals("Series");
            seasonsField.setEnabled(isSeries);
            episodesField.setEnabled(isSeries);
        });

        JTextArea outputArea = new JTextArea(10, 40);
        outputArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(outputArea);

        JButton submitButton = new JButton("Submit");
        JButton clearButton = new JButton("Clear");

        submitButton.addActionListener(e -> {
            try {
                StringBuilder output = new StringBuilder("Movie Details:\n");
                for (int i = 0; i < labels.length; i++) {
                    if (fields[i].getText().trim().isEmpty()) {
                        throw new Exception(labels[i] + " cannot be empty.");
                    }
                    output.append(labels[i]).append(": ").append(fields[i].getText().trim()).append("\n");
                }

                int releaseYear = Integer.parseInt(fields[2].getText().trim());
                int duration = Integer.parseInt(fields[7].getText().trim());
                double imdbRating = Double.parseDouble(fields[8].getText().trim());
                String viewerRestriction = fields[9].getText().trim(); // Now accepts text values

                if (imdbRating < 0.0 || imdbRating > 10.0) {
                    throw new Exception("IMDb Rating must be between 0.0 and 10.0.");
                }
                if (releaseYear <= 0 || duration <= 0) {
                    throw new Exception("Numeric values must be positive.");
                }
                
                output.append("Content Type: ").append(contentType.getSelectedItem()).append("\n");
                
                if (contentType.getSelectedItem().equals("Series")) {
                    int seasons = Integer.parseInt(seasonsField.getText().trim());
                    int episodes = Integer.parseInt(episodesField.getText().trim());
                    if (seasons <= 0 || episodes <= 0) {
                        throw new Exception("Seasons and Episodes must be positive numbers.");
                    }
                    output.append("Seasons: ").append(seasons).append("\n");
                    output.append("Episodes: ").append(episodes).append("\n");
                }
                
                outputArea.setText(output.toString());
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Please enter valid numeric values where required.", "Input Error", JOptionPane.ERROR_MESSAGE);
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(frame, ex.getMessage(), "Input Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        clearButton.addActionListener(e -> {
            for (JTextField field : fields) field.setText("");
            seasonsField.setText("");
            episodesField.setText("");
            outputArea.setText("");
        });

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(submitButton);
        buttonPanel.add(clearButton);

        frame.add(inputPanel, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);
        frame.add(scrollPane, BorderLayout.NORTH);
        frame.setVisible(true);
    }
}

