// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	let disposable = vscode.commands.registerCommand('extension.createJsonFile', async () => {
		const workspaceFolders = vscode.workspace.workspaceFolders;
		if (!workspaceFolders) {
			vscode.window.showErrorMessage('No workspace folders are open.');
			return;
		}
		const fileName = await vscode.window.showInputBox({ prompt: 'Enter filename' });
           if (!fileName) {
               return;
           }
		   const workspacePath = workspaceFolders[0].uri.fsPath;
           const newFilePath = path.join(workspacePath, fileName);

           if (fs.existsSync(newFilePath)) {
               vscode.window.showErrorMessage(`The file ${fileName} already exists.`);
               return;
           }

           fs.writeFileSync(newFilePath, '{}', 'utf8');
           const textDocument = await vscode.workspace.openTextDocument(newFilePath);
           await vscode.window.showTextDocument(textDocument);
           vscode.window.showInformationMessage(`Created a new JSON file: ${fileName}`);
       });

       context.subscriptions.push(disposable);
   }

// This method is called when your extension is deactivated
export function deactivate() {}
